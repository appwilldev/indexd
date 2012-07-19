#include<Python.h>
#include<scws.h>

typedef struct {
    PyObject_HEAD
    scws_t scws;
} SCWSObject;

static int scws_init(SCWSObject* self, PyObject *args, PyObject *kwds){
    static char *kwlist[] = {"dict", "rules", "charset", NULL};
    char *dict;
    char *rules = NULL;
    char *charset = "utf-8";
    scws_t s; /* scws_t is a pointer type.... */
    int st;

    if(!PyArg_ParseTupleAndKeywords(args, kwds, "s|ss", kwlist,
		&dict, &rules, &charset))
	return -1;

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
    st = scws_set_dict(s, dict, SCWS_XDICT_XDB);
    if(rules)
	scws_set_rule(s, rules);
    Py_END_ALLOW_THREADS

    if(st < 0){
	PyErr_SetString(PyExc_EnvironmentError, "failed to set dict");
	Py_BEGIN_ALLOW_THREADS
	scws_free(s);
	Py_END_ALLOW_THREADS
	return -1;
    }

    return 0;
}

static PyObject* scws_call(SCWSObject* self, PyObject *args, PyObject *kwds){
    char* sentence;
    int len;
    scws_t s;
    scws_res_t result, cursor;
    PyObject *ret;

    if(!PyArg_ParseTuple(args, "s#", &sentence, &len)){
	return NULL;
    }

    s = self->scws;
    Py_BEGIN_ALLOW_THREADS
    scws_send_text(s, sentence, len);
    Py_END_ALLOW_THREADS

    ret = PyList_New(0);
    for(cursor = result = scws_get_result(s); cursor != NULL; cursor = cursor->next){
	PyList_Append(ret, Py_BuildValue("s#", sentence + cursor->off /* means offset */, cursor->len));
    }
    Py_BEGIN_ALLOW_THREADS
    scws_free_result(result);
    Py_END_ALLOW_THREADS

    return ret;
}

static void scws_dealloc(SCWSObject *self){
    Py_BEGIN_ALLOW_THREADS
    scws_free(self->scws);
    Py_END_ALLOW_THREADS
}

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
    "SCWS Objects",           /* tp_doc            */
    0,                        /* tp_traverse       */
    0,                        /* tp_clear          */
    0,                        /* tp_richcompare    */
    0,                        /* tp_weaklistoffset */
    0,                        /* tp_iter           */
    0,                        /* tp_iternext       */
    0,                        /* tp_methods        */
    0,                        /* tp_members        */
    0,                        /* tp_getset         */
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
    PyObject* m;

    if (PyType_Ready(&SCWSObjectType) < 0)
	return;

    m = Py_InitModule3("scws", NULL, "A simple Python binding for SCWS.");
    if (m == NULL)
	return;

    Py_INCREF(&SCWSObjectType);
    PyModule_AddObject(m, "SCWS", (PyObject *)&SCWSObjectType);
}
