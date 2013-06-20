#include<Python.h>
#include<scws/scws.h>

typedef struct {
    PyObject_HEAD
    scws_t scws;
    int ignore;
} SCWSObject;

#define scws_doc "SCWS Objects.\n\n" \
    "Initialized with a \"dict\" file path and optional " \
    "\"rules\" file path and \"charset\" (default is " \
    "\"utf-8\")."

static PyObject *DictError;

static int scws_init(SCWSObject* self, PyObject *args, PyObject *kwds){
    static char *kwlist[] = {"dict", "rules", "charset", "dicttype", NULL};
    char *dict;
    char *rules = NULL;
    char *charset = "utf-8";
    int dicttype = SCWS_XDICT_XDB;
    scws_t s; /* scws_t is a pointer type.... */
    int st;

    if(!PyArg_ParseTupleAndKeywords(args, kwds, "s|zsi", kwlist,
                &dict, &rules, &charset, &dicttype))
        return -1;

    self->scws = NULL;
    self->ignore = 0;
    Py_BEGIN_ALLOW_THREADS
    s = scws_new();
    Py_END_ALLOW_THREADS
    if(!s){
        /* the doc says it's because insufficient memory */
        PyErr_SetString(PyExc_MemoryError, "failed to init the scws struct");
        return -1;
    }
    self->scws = s;
    Py_BEGIN_ALLOW_THREADS
    scws_set_charset(s, charset); /* fallback to "gbk" if error.... */
    st = scws_set_dict(s, dict, dicttype);
    if(rules)
        scws_set_rule(s, rules);
    Py_END_ALLOW_THREADS

    if(st < 0){
        PyErr_Format(DictError, "failed to add dict file \"%s\" with dict type %d", dict, dicttype);
        return -1;
    }

    return 0;
}

static PyObject* scws_call(SCWSObject* self, PyObject *args, PyObject *kwds){
    char* sentence;
    int len;
    scws_t s;
    scws_res_t result, cursor;
    PyObject *ret, *o;

    if(!PyArg_ParseTuple(args, "s#", &sentence, &len)){
        return NULL;
    }

    s = self->scws;
    Py_BEGIN_ALLOW_THREADS
    scws_send_text(s, sentence, len);
    Py_END_ALLOW_THREADS

    ret = PyList_New(0);
    while((result = scws_get_result(s)) != NULL){
        for(cursor = result; cursor != NULL; cursor = cursor->next){
            o = PyString_FromStringAndSize(sentence + cursor->off /* means offset */, cursor->len);
            PyList_Append(ret, o);
            Py_DECREF(o);
        }
        Py_BEGIN_ALLOW_THREADS
        scws_free_result(result);
        Py_END_ALLOW_THREADS
    }

    return ret;
}

static void scws_dealloc(SCWSObject *self){
    if(self->scws){
        scws_free(self->scws);
    }
    self->ob_type->tp_free(self);
}

static PyObject *my_scws_get_ignore(SCWSObject *self, void *x){
    return PyBool_FromLong(self->ignore);
}

static int my_scws_set_ignore(SCWSObject *self, PyObject *val, void *x){
    if(!PyBool_Check(val)){
        PyErr_SetString(PyExc_TypeError, "ignore should be a boolean value");
        return -1;
    }
    if(val == Py_True){
        if(self->ignore != 1){
            scws_set_ignore(self->scws, 1);
            self->ignore = 1;
        }
    }else{
        if(self->ignore != 0){
            scws_set_ignore(self->scws, 0);
            self->ignore = 0;
        }
    }
    return 0;
}

static PyObject *my_scws_add_dict(SCWSObject *self, PyObject *args){
    char *dict;
    int dicttype = SCWS_XDICT_XDB;
    scws_t s;
    int st;

    if(!PyArg_ParseTuple(args, "s|i", &dict, &dicttype))
        return NULL;

    s = self->scws;
    Py_BEGIN_ALLOW_THREADS
    st = scws_add_dict(s, dict, dicttype);
    Py_END_ALLOW_THREADS
    if(st < 0){
        PyErr_Format(DictError, "failed to add dict file \"%s\" with dict type %d", dict, dicttype);
        return NULL;
    }

    Py_RETURN_NONE;
};

static PyGetSetDef scws_getsetdef[] = {
    {"ignore", (getter)my_scws_get_ignore, (setter)my_scws_set_ignore, "whether to ignore punctuations", NULL},
    {NULL, NULL, NULL, NULL, NULL},
};

static PyMethodDef scws_methods[] = {
    {"add_dict", (PyCFunction)my_scws_add_dict, METH_VARARGS, "add additional dictionaries. Arguments are dictfile name and type."},
    {NULL, NULL, 0, NULL},
};

static PyTypeObject SCWSObjectType = {
    PyObject_HEAD_INIT(NULL)
    0,                        /* ob_size           */
    "scws.SCWS",              /* tp_name           */
    sizeof(SCWSObject),       /* tp_basicsize      */
    0,                        /* tp_itemsize       */
    (destructor)scws_dealloc, /* tp_dealloc        */
    0,                        /* tp_print          */
    0,                        /* tp_getattr        */
    0,                        /* tp_setattr        */
    0,                        /* tp_compare        */
    0,                        /* tp_repr           */
    0,                        /* tp_as_number      */
    0,                        /* tp_as_sequence    */
    0,                        /* tp_as_mapping     */
    0,                        /* tp_hash           */
    (ternaryfunc)scws_call,   /* tp_call           */
    0,                        /* tp_str            */
    0,                        /* tp_getattro       */
    0,                        /* tp_setattro       */
    0,                        /* tp_as_buffer      */
    Py_TPFLAGS_DEFAULT,       /* tp_flags          */
    scws_doc,                 /* tp_doc            */
    0,                        /* tp_traverse       */
    0,                        /* tp_clear          */
    0,                        /* tp_richcompare    */
    0,                        /* tp_weaklistoffset */
    0,                        /* tp_iter           */
    0,                        /* tp_iternext       */
    scws_methods,             /* tp_methods        */
    0,                        /* tp_members        */
    scws_getsetdef,           /* tp_getset         */
    0,                        /* tp_base           */
    0,                        /* tp_dict           */
    0,                        /* tp_descr_get      */
    0,                        /* tp_descr_set      */
    0,                        /* tp_dictoffset     */
    (initproc)scws_init,      /* tp_init           */
    0,                        /* tp_alloc          */
    PyType_GenericNew,        /* tp_new            */
};

PyMODINIT_FUNC initscws(void){
    PyObject *m;

    if (PyType_Ready(&SCWSObjectType) < 0)
        return;

    m = Py_InitModule3("scws", NULL, "A simple Python binding for SCWS.");
    if (m == NULL)
        return;

    Py_INCREF(&SCWSObjectType);

    DictError = PyErr_NewException("scws.DictError", NULL, NULL);

    PyModule_AddObject(m, "SCWS", (PyObject *)&SCWSObjectType);
    PyModule_AddObject(m, "DictError", DictError);
    PyModule_AddIntMacro(m, SCWS_XDICT_XDB);
    PyModule_AddIntMacro(m, SCWS_XDICT_TXT);
    PyModule_AddIntMacro(m, SCWS_XDICT_MEM);
}
