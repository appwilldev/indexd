Client:

1343008114.41 import begin.
1343008114.41 creating database...
1343008114.88 start indexing...
1343008197.57 indexing finished.
1343008197.57 all done.
         5572778 function calls (5572693 primitive calls) in 83.182 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   131075   72.166    0.001   72.166    0.001 {method 'recv' of '_socket.socket' objects}
  1441748    1.910    0.000    1.919    0.000 {method 'decode' of 'str' objects}
    65535    1.564    0.000    1.910    0.000 csv.py:100(next)
    65534    1.373    0.000    3.592    0.000 importen.py:33(dict2unicode)
   131074    1.222    0.000    1.222    0.000 {method 'sendall' of '_socket.socket' objects}
   131075    0.708    0.000   73.065    0.001 util.py:15(recvbytes)
    65537    0.608    0.000    2.888    0.000 util.py:32(write_response)
    65537    0.503    0.000    0.503    0.000 {ujson.dumps}
  1572950    0.327    0.000    0.327    0.000 {isinstance}
    65537    0.322    0.000   73.825    0.001 util.py:41(read_response)
    65535    0.321    0.000    5.824    0.000 importen.py:50(parse_csv_file)
    65537    0.256    0.000   77.024    0.001 client.py:49(do_cmd)
   131075    0.206    0.000    1.484    0.000 socket.py:223(meth)
        1    0.181    0.181   83.163   83.163 importen.py:56(main)
   131069    0.168    0.000    0.168    0.000 csv.py:86(fieldnames)
    65537    0.152    0.000    0.152    0.000 {ujson.loads}
    65534    0.150    0.000    0.150    0.000 {zip}
    65537    0.146    0.000    0.230    0.000 util.py:9(parse_netint)
    65534    0.133    0.000   76.680    0.001 client.py:39(insert)
   131431    0.095    0.000    0.095    0.000 {method 'append' of 'list' objects}
328216/328199    0.086    0.000    0.086    0.000 {len}
    65537    0.085    0.000    0.085    0.000 {_struct.unpack}
    65537    0.076    0.000    0.578    0.000 util.py:29(tojson)
    65537    0.073    0.000    0.073    0.000 {_struct.pack}
    65540    0.059    0.000    0.059    0.000 {method 'items' of 'dict' objects}
    65537    0.056    0.000    0.208    0.000 util.py:26(fromjson)
   131139    0.055    0.000    0.055    0.000 {getattr}
    65537    0.054    0.000    0.054    0.000 {method 'update' of 'dict' objects}
   131076    0.050    0.000    0.050    0.000 {method 'join' of 'str' objects}
    65537    0.046    0.000    0.119    0.000 util.py:12(pack_netint)
        1    0.009    0.009    0.010    0.010 {__import__}
        1    0.007    0.007   83.182   83.182 importen.py:4(<module>)
        1    0.002    0.002    0.003    0.003 socket.py:45(<module>)
        1    0.002    0.002    0.011    0.011 client.py:3(<module>)
        1    0.001    0.001    0.002    0.002 csv.py:4(<module>)
        1    0.001    0.001    0.002    0.002 collections.py:1(<module>)
        1    0.001    0.001    0.001    0.001 heapq.py:31(<module>)
        1    0.001    0.001    0.005    0.005 ConfigParser.py:88(<module>)
        1    0.000    0.000    0.006    0.006 util.py:3(<module>)
        1    0.000    0.000    0.000    0.000 {method 'connect' of '_socket.socket' objects}
     16/6    0.000    0.000    0.001    0.000 sre_parse.py:379(_parse)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
     29/5    0.000    0.000    0.001    0.000 sre_compile.py:32(_compile)
        1    0.000    0.000    0.000    0.000 latin_1.py:8(<module>)
      171    0.000    0.000    0.000    0.000 sre_parse.py:182(__next)
        1    0.000    0.000    0.000    0.000 exceptions.py:3(<module>)
       10    0.000    0.000    0.000    0.000 sre_compile.py:207(_optimize_charset)
    41/17    0.000    0.000    0.000    0.000 sre_parse.py:140(getwidth)
      111    0.000    0.000    0.000    0.000 sre_parse.py:130(__getitem__)
      125    0.000    0.000    0.000    0.000 sre_parse.py:201(get)
        1    0.000    0.000    0.000    0.000 {dir}
        1    0.000    0.000    0.000    0.000 socket.py:179(_socketobject)
        5    0.000    0.000    0.000    0.000 sre_compile.py:361(_compile_info)
        1    0.000    0.000    0.000    0.000 os.py:35(_get_exports_list)
     15/5    0.000    0.000    0.001    0.000 sre_parse.py:301(_parse_sub)
        5    0.000    0.000    0.002    0.000 re.py:229(_compile)
      100    0.000    0.000    0.000    0.000 sre_parse.py:195(match)
        1    0.000    0.000    0.010    0.010 __init__.py:71(search_function)
       10    0.000    0.000    0.000    0.000 sre_compile.py:178(_compile_charset)
        1    0.000    0.000    0.000    0.000 __init__.py:49(normalize_encoding)
        2    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x1020b5f30}
        1    0.000    0.000    0.000    0.000 {open}
        1    0.000    0.000    0.000    0.000 socket.py:185(__init__)
        1    0.000    0.000    0.000    0.000 abc.py:86(__new__)
       12    0.000    0.000    0.000    0.000 sre_compile.py:354(_simple)
        5    0.000    0.000    0.002    0.000 sre_compile.py:495(compile)
       26    0.000    0.000    0.000    0.000 {setattr}
        5    0.000    0.000    0.001    0.000 sre_parse.py:663(parse)
        7    0.000    0.000    0.000    0.000 sre_parse.py:216(isname)
       60    0.000    0.000    0.000    0.000 {min}
        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
       39    0.000    0.000    0.000    0.000 sre_parse.py:138(append)
        1    0.000    0.000    0.001    0.001 client.py:11(__init__)
       29    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
       10    0.000    0.000    0.000    0.000 sre_parse.py:257(_escape)
        1    0.000    0.000    0.000    0.000 collections.py:46(OrderedDict)
        1    0.000    0.000    0.000    0.000 socket.py:192(close)
       59    0.000    0.000    0.000    0.000 sre_parse.py:126(__len__)
        1    0.000    0.000    0.000    0.000 {method 'send' of '_socket.socket' objects}
        1    0.000    0.000    0.002    0.002 ConfigParser.py:223(RawConfigParser)
        9    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
        1    0.000    0.000    0.000    0.000 posixpath.py:80(split)
        1    0.000    0.000    0.000    0.000 socket.py:235(_fileobject)
        2    0.000    0.000    0.000    0.000 {_csv.register_dialect}
        5    0.000    0.000    0.001    0.000 sre_compile.py:480(_code)
        5    0.000    0.000    0.000    0.000 {_sre.compile}
        1    0.000    0.000    0.000    0.000 latin_1.py:41(getregentry)
        1    0.000    0.000    0.000    0.000 csv.py:74(__init__)
        9    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
        1    0.000    0.000    0.000    0.000 codecs.py:77(__new__)
        1    0.000    0.000    0.000    0.000 csv.py:73(DictReader)
       34    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
        1    0.000    0.000    0.000    0.000 {_csv.reader}
        3    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
        1    0.000    0.000    0.000    0.000 abc.py:89(<genexpr>)
       32    0.000    0.000    0.000    0.000 sre_parse.py:210(isident)
        1    0.000    0.000    0.000    0.000 posixpath.py:60(join)
       10    0.000    0.000    0.000    0.000 sre_compile.py:474(isstring)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        5    0.000    0.000    0.000    0.000 sre_parse.py:178(__init__)
        1    0.000    0.000    0.001    0.001 client.py:26(setdb)
        1    0.000    0.000    0.000    0.000 collections.py:326(Counter)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:112(Error)
        1    0.000    0.000    0.476    0.476 client.py:32(createdb)
        5    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 client.py:23(setmode)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:548(ConfigParser)
        1    0.000    0.000    0.000    0.000 latin_1.py:13(Codec)
        9    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.000    0.000 collections.py:20(_recursive_repr)
        5    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
       24    0.000    0.000    0.000    0.000 sre_compile.py:24(_identityfunction)
       12    0.000    0.000    0.000    0.000 sre_parse.py:134(__setitem__)
        1    0.000    0.000    0.000    0.000 pprint.py:81(PrettyPrinter)
        1    0.000    0.000    0.000    0.000 csv.py:26(Dialect)
        1    0.000    0.000    0.000    0.000 client.py:17(close)
        2    0.000    0.000    0.000    0.000 sre_parse.py:225(_class_escape)
        5    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       25    0.000    0.000    0.000    0.000 {ord}
        1    0.000    0.000    0.000    0.000 client.py:10(Client)
        1    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 csv.py:123(DictWriter)
        2    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 socket.py:167(_closedsocket)
        1    0.000    0.000    0.000    0.000 latin_1.py:20(IncrementalEncoder)
        1    0.000    0.000    0.000    0.000 csv.py:162(Sniffer)
        1    0.000    0.000    0.000    0.000 latin_1.py:24(IncrementalDecoder)
        1    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 {method 'translate' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
        1    0.000    0.000    0.000    0.000 csv.py:57(excel)
        1    0.000    0.000    0.000    0.000 latin_1.py:34(StreamConverter)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:644(SafeConfigParser)
        1    0.000    0.000    0.000    0.000 importen.py:25(thisdir)
        1    0.000    0.000    0.000    0.000 exceptions.py:13(AWIPErrorWithCode)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:210(MissingSectionHeaderError)
        1    0.000    0.000    0.000    0.000 csv.py:83(__iter__)
        1    0.000    0.000    0.000    0.000 latin_1.py:28(StreamWriter)
        1    0.000    0.000    0.000    0.000 exceptions.py:56(AWIPServerError)
        5    0.000    0.000    0.002    0.000 re.py:188(compile)
        1    0.000    0.000    0.000    0.000 latin_1.py:31(StreamReader)
        1    0.000    0.000    0.000    0.000 exceptions.py:38(AWIPClientError)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:183(InterpolationSyntaxError)
        1    0.000    0.000    0.000    0.000 util.py:52(CasedConfigParser)
        1    0.000    0.000    0.000    0.000 constants.py:3(<module>)
        1    0.000    0.000    0.000    0.000 exceptions.py:5(AWIPError)
        1    0.000    0.000    0.000    0.000 exceptions.py:41(AWIPHandshakeFailed)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:198(ParsingError)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:162(InterpolationError)
        1    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:146(DuplicateSectionError)
        1    0.000    0.000    0.000    0.000 exceptions.py:54(AWIPRequestInvalid)
        1    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 exceptions.py:59(AWIPOperationError)
        1    0.000    0.000    0.000    0.000 csv.py:67(excel_tab)
        2    0.000    0.000    0.000    0.000 {max}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:139(NoSectionError)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:153(NoOptionError)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 exceptions.py:47(AWIPClientDisconnected)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:170(InterpolationMissingOptionError)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:187(InterpolationDepthError)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Server:

         9367316 function calls (9301016 primitive calls) in 95.329 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    65534   38.531    0.001   38.531    0.001 {_xapian.WritableDatabase_replace_document}
  65545/2   11.715    0.000    0.000    0.000 hub.py:366(switch)
   262136   11.633    0.000   11.633    0.000 {_xapian.TermGenerator_index_text}
      2/1    9.249    4.625   94.128   94.128 baseserver.py:274(serve_forever)
        1    1.715    1.715    1.715    1.715 {_xapian.WritableDatabase_commit}
    65534    1.715    0.000   59.180    0.001 xapiandb.py:217(add_document)
   131075    1.452    0.000    1.452    0.000 {method 'send' of '_socket.socket' objects}
    65534    1.402    0.000    1.402    0.000 {_xapian.TermGenerator_set_document}
    65538    1.110    0.000   82.954    0.001 server.py:89(handle_request)
   196619    1.085    0.000    1.085    0.000 {method 'recv' of '_socket.socket' objects}
   131076    0.913    0.000   14.754    0.000 socket.py:369(recv)
   131080    0.749    0.000    1.856    0.000 _abcoll.py:483(update)
   131075    0.742    0.000    2.806    0.000 socket.py:460(sendall)
   131076    0.685    0.000   15.569    0.000 util.py:15(recvbytes)
   131071    0.659    0.000    0.659    0.000 {ujson.dumps}
    65545    0.583    0.000    1.385    0.000 collections.py:58(__init__)
   196645    0.472    0.000    0.472    0.000 collections.py:76(__setitem__)
    65537    0.462    0.000    0.462    0.000 {ujson.loads}
        1    0.444    0.444    0.444    0.444 {_xapian.new_WritableDatabase}
    65535    0.413    0.000    3.860    0.000 ConfigParser.py:334(items)
   131074    0.386    0.000    0.410    0.000 ConfigParser.py:318(get)
    65537    0.346    0.000    3.647    0.000 util.py:32(write_response)
    65543    0.332    0.000   12.472    0.000 hub.py:380(wait)
   131076    0.316    0.000    0.316    0.000 request.py:12(get_required_field)
   262784    0.308    0.000    0.308    0.000 {getattr}
   461703    0.306    0.000    0.600    0.000 {isinstance}
    65534    0.283    0.000   59.763    0.001 server.py:161(handle_cmd_insert)
      289    0.282    0.001    0.282    0.001 {posix.stat}
   327730    0.278    0.000    0.278    0.000 _weakrefset.py:68(__contains__)
   196623    0.272    0.000    0.272    0.000 __init__.py:1310(getEffectiveLevel)
   131075    0.262    0.000    0.262    0.000 socket.py:198(_get_memory)
   524316    0.247    0.000    0.247    0.000 collections.py:97(__iter__)
    65538    0.234    0.000   16.457    0.000 util.py:41(read_response)
   196623    0.226    0.000    0.498    0.000 __init__.py:1324(isEnabledFor)
    65535    0.222    0.000    1.606    0.000 collections.py:178(copy)
196637/196635    0.210    0.000    0.407    0.000 abc.py:148(__subclasscheck__)
   131075    0.209    0.000    1.661    0.000 socket.py:434(send)
        1    0.208    0.208   84.877   84.877 server.py:50(__init__)
    65534    0.191    0.000    0.191    0.000 {_xapian.Document_add_boolean_term}
    65535    0.185    0.000    0.329    0.000 xapiandb.py:41(_parse_indexing_fields)
    65537    0.178    0.000    4.069    0.000 server.py:114(reply)
   131080    0.176    0.000    0.294    0.000 abc.py:128(__instancecheck__)
856207/856073    0.173    0.000    0.173    0.000 {len}
    65543    0.166    0.000   12.638    0.000 socket.py:275(_wait)
   131071    0.159    0.000    0.818    0.000 util.py:29(tojson)
    65543    0.152    0.000    0.231    0.000 _abcoll.py:368(items)
   131088    0.141    0.000    0.141    0.000 {sys.exc_clear}
    65534    0.134    0.000    0.134    0.000 {_xapian.new_Document}
    65534    0.128    0.000    0.128    0.000 {_xapian.Document_set_data}
    65535    0.121    0.000   60.359    0.001 server.py:28(wrapper)
   131075    0.119    0.000    0.476    0.000 __init__.py:1110(debug)
    65535    0.118    0.000    0.133    0.000 collections.py:86(__delitem__)
    65534    0.116    0.000   60.000    0.001 server.py:19(wrapper)
        1    0.103    0.103    0.170    0.170 xapiandb.py:3(<module>)
    66140    0.101    0.000    0.101    0.000 {method 'split' of 'str' objects}
   131076    0.099    0.000    0.415    0.000 request.py:9(__getattr__)
    65534    0.093    0.000    0.271    0.000 __init__.py:1263(__init__)
   131068    0.092    0.000    0.092    0.000 {_xapian.TermGenerator_increase_termpos}
    65537    0.090    0.000    0.140    0.000 util.py:9(parse_netint)
    65544    0.085    0.000    0.085    0.000 {method 'start' of 'gevent.core.io' objects}
    65537    0.084    0.000    0.084    0.000 {_struct.pack}
    65535    0.073    0.000    0.239    0.000 request.py:19(get_type)
      2/1    0.070    0.035   94.128   94.128 indexd.py:4(<module>)
    65548    0.066    0.000    0.207    0.000 __init__.py:1122(info)
   131089    0.064    0.000    0.064    0.000 {sys.exc_info}
        1    0.064    0.064    1.030    1.030 server.py:3(<module>)
   135627    0.063    0.000    0.063    0.000 {method 'append' of 'list' objects}
    65534    0.061    0.000    0.300    0.000 request.py:38(get_dict)
    65537    0.055    0.000    0.139    0.000 util.py:12(pack_netint)
        1    0.053    0.053    0.098    0.098 pkg_resources.py:215(get_build_platform)
    65537    0.052    0.000    0.514    0.000 util.py:26(fromjson)
    65537    0.050    0.000    0.050    0.000 {_struct.unpack}
        2    0.047    0.023    0.047    0.023 {imp.load_module}
    65537    0.046    0.000    0.046    0.000 request.py:6(__init__)
        7    0.044    0.006    0.044    0.006 {open}
    65534    0.044    0.000    0.044    0.000 {_xapian.Document_swiginit}
        1    0.044    0.044    0.099    0.099 plistlib.py:400(parse)
   131656    0.044    0.000    0.044    0.000 {method 'strip' of 'str' objects}
        8    0.040    0.005    0.067    0.008 {__import__}
   131414    0.037    0.000    0.037    0.000 {method 'join' of 'str' objects}
        1    0.034    0.034    0.034    0.034 greenlet.py:3(<module>)
        1    0.032    0.032    0.037    0.037 __init__.py:24(<module>)
   131124    0.032    0.000    0.032    0.000 {method 'items' of 'dict' objects}
        2    0.030    0.015    0.030    0.015 {imp.load_dynamic}
        1    0.030    0.030    0.679    0.679 _util.py:1(__bootstrap__)
        1    0.028    0.028    0.028    0.028 expat.py:1(<module>)
    65545    0.028    0.000    0.028    0.000 {gevent._util.set_exc_info}
    65534    0.026    0.000    0.027    0.000 xapiandb.py:186(load_termgenerator)
        1    0.026    0.026    0.026    0.026 __init__.py:17(<module>)
        1    0.025    0.025    0.762    0.762 __init__.py:7(<module>)
   131092    0.025    0.000    0.025    0.000 {greenlet.getcurrent}
   131088    0.024    0.000    0.024    0.000 util.py:53(optionxform)
    65544    0.022    0.000    0.022    0.000 {method 'stop' of 'gevent.core.io' objects}
        1    0.021    0.021    0.053    0.053 __init__.py:13(<module>)
        1    0.019    0.019    0.035    0.035 beautifullog.py:5(enable_pretty_logging)
        1    0.019    0.019    0.020    0.020 util.py:5(<module>)
       65    0.017    0.000    0.017    0.000 {imp.find_module}
        1    0.015    0.015    0.015    0.015 __init__.py:11(<module>)
       28    0.015    0.001    0.015    0.001 {posix.listdir}
    65564    0.014    0.000    0.014    0.000 {method 'pop' of 'dict' objects}
        1    0.013    0.013    0.014    0.014 io.py:34(<module>)
        6    0.013    0.002    0.013    0.002 {method 'close' of 'file' objects}
        1    0.011    0.011    0.019    0.019 sysconfig.py:259(parse_makefile)
        1    0.010    0.010    0.112    0.112 platform.py:770(_mac_ver_xml)
      603    0.009    0.000    0.009    0.000 {posix.lstat}
        1    0.008    0.008    0.031    0.031 server.py:2(<module>)
      908    0.005    0.000    0.008    0.000 posixpath.py:60(join)
      447    0.005    0.000    0.007    0.000 text_file.py:161(readline)
   131/40    0.004    0.000    0.011    0.000 sre_parse.py:379(_parse)
      186    0.003    0.000    0.033    0.000 pkg_resources.py:1686(find_on_path)
       76    0.003    0.000    0.005    0.000 pkg_resources.py:2257(insert_on)
       71    0.003    0.000    0.003    0.000 pkg_resources.py:2530(_get_mro)
       84    0.003    0.000    0.023    0.000 posixpath.py:355(realpath)
   250/36    0.003    0.000    0.006    0.000 sre_compile.py:32(_compile)
     2952    0.002    0.000    0.002    0.000 {built-in method match}
     1183    0.002    0.000    0.002    0.000 sre_parse.py:182(__next)
     5839    0.002    0.000    0.002    0.000 {method 'endswith' of 'str' objects}
     4123    0.002    0.000    0.002    0.000 {method 'startswith' of 'str' objects}
     2610    0.002    0.000    0.002    0.000 {method 'readline' of 'file' objects}
  361/147    0.002    0.000    0.002    0.000 sre_parse.py:140(getwidth)
        1    0.002    0.002    0.123    0.123 pkg_resources.py:206(_macosx_vers)
        1    0.002    0.002    0.003    0.003 sysconfig.py:224(parse_config_h)
        1    0.001    0.001    0.002    0.002 socket.py:45(<module>)
        1    0.001    0.001    0.002    0.002 heapq.py:31(<module>)
        1    0.001    0.001    0.004    0.004 collections.py:1(<module>)
        1    0.001    0.001    0.001    0.001 baseserver.py:1(<module>)
      152    0.001    0.000    0.007    0.000 pkg_resources.py:2068(from_location)
     2674    0.001    0.000    0.001    0.000 {method 'lower' of 'str' objects}
      603    0.001    0.000    0.011    0.000 posixpath.py:130(islink)
      152    0.001    0.000    0.004    0.000 pkg_resources.py:2054(__init__)
     1014    0.001    0.000    0.002    0.000 sre_parse.py:130(__getitem__)
        1    0.001    0.001    0.001    0.001 ssl.py:56(<module>)
      152    0.001    0.000    0.003    0.000 pkg_resources.py:506(add)
      308    0.001    0.000    0.001    0.000 {built-in method sub}
       87    0.001    0.000    0.002    0.000 posixpath.py:312(normpath)
        1    0.001    0.001    0.024    0.024 util.py:16(get_platform)
       79    0.001    0.000    0.281    0.004 genericpath.py:15(exists)
       88    0.001    0.000    0.001    0.000 sre_compile.py:207(_optimize_charset)
      354    0.001    0.000    0.022    0.000 re.py:229(_compile)
      456    0.001    0.000    0.001    0.000 pkg_resources.py:2098(key)
        1    0.001    0.001    0.005    0.005 threading.py:1(<module>)
        1    0.001    0.001    0.022    0.022 socket.py:32(<module>)
        1    0.001    0.001    0.001    0.001 spawn.py:7(<module>)
        1    0.001    0.001    0.001    0.001 errors.py:9(<module>)
      951    0.001    0.000    0.003    0.000 sre_parse.py:201(get)
     1623    0.001    0.000    0.004    0.000 pkg_resources.py:1831(_normalize_cached)
       64    0.001    0.000    0.038    0.001 pkgutil.py:176(find_module)
        1    0.001    0.001    0.703    0.703 hub.py:3(<module>)
        1    0.001    0.001    0.003    0.003 plistlib.py:51(<module>)
       76    0.001    0.000    0.375    0.005 pkg_resources.py:2166(activate)
        1    0.001    0.001    0.001    0.001 {method 'bind' of '_socket.socket' objects}
   118/36    0.001    0.000    0.011    0.000 sre_parse.py:301(_parse_sub)
       77    0.001    0.000    0.356    0.005 {map}
      600    0.001    0.000    0.001    0.000 stat.py:55(S_ISLNK)
        1    0.001    0.001    0.641    0.641 pkg_resources.py:14(<module>)
       36    0.001    0.000    0.003    0.000 sre_compile.py:361(_compile_info)
     1346    0.001    0.000    0.001    0.000 {method 'find' of 'str' objects}
       13    0.001    0.000    0.001    0.000 pkg_resources.py:1419(_index)
       80    0.001    0.000    0.001    0.000 posixpath.py:118(dirname)
       66    0.001    0.000    0.057    0.001 pkg_resources.py:1743(_handle_ns)
        1    0.000    0.000    0.001    0.001 argparse.py:62(<module>)
       76    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
      230    0.000    0.000    0.001    0.000 pkg_resources.py:2198(__getattr__)
       40    0.000    0.000    0.038    0.001 pkg_resources.py:428(add_entry)
       76    0.000    0.000    0.024    0.000 pkg_resources.py:1795(fixup_namespace_packages)
      308    0.000    0.000    0.002    0.000 re.py:144(sub)
     1260    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      152    0.000    0.000    0.001    0.000 genericpath.py:85(_splitext)
        2    0.000    0.000    0.001    0.001 ConfigParser.py:456(_read)
       78    0.000    0.000    0.311    0.004 pkg_resources.py:2161(_get_metadata)
       88    0.000    0.000    0.002    0.000 sre_compile.py:178(_compile_charset)
      106    0.000    0.000    0.001    0.000 pkgutil.py:358(get_importer)
        1    0.000    0.000    0.001    0.001 socket.py:223(socket)
      693    0.000    0.000    0.001    0.000 sre_parse.py:195(match)
      798    0.000    0.000    0.000    0.000 stat.py:24(S_IFMT)
      463    0.000    0.000    0.001    0.000 sre_parse.py:138(append)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
      761    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      188    0.000    0.000    0.002    0.000 genericpath.py:38(isdir)
      871    0.000    0.000    0.000    0.000 {built-in method group}
      416    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {_xapian.Database_close}
      408    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'read' of 'file' objects}
      501    0.000    0.000    0.000    0.000 sre_parse.py:126(__len__)
        1    0.000    0.000    0.003    0.003 ConfigParser.py:88(<module>)
       36    0.000    0.000    0.021    0.001 sre_compile.py:495(compile)
      525    0.000    0.000    0.000    0.000 {min}
       65    0.000    0.000    0.281    0.004 pkg_resources.py:1275(_has)
      111    0.000    0.000    0.000    0.000 sre_compile.py:354(_simple)
       72    0.000    0.000    0.283    0.004 pkg_resources.py:1172(has_metadata)
       86    0.000    0.000    0.001    0.000 pkg_resources.py:1231(_fn)
       77    0.000    0.000    0.000    0.000 pkg_resources.py:493(__iter__)
       36    0.000    0.000    0.011    0.000 sre_parse.py:663(parse)
        1    0.000    0.000    0.000    0.000 __init__.py:280(InvalidArgumentError)
      150    0.000    0.000    0.001    0.000 pkg_resources.py:1116(safe_version)
       71    0.000    0.000    0.003    0.000 pkg_resources.py:2537(_find_adapter)
        2    0.000    0.000    0.000    0.000 socket.py:294(accept)
       76    0.000    0.000    0.376    0.005 pkg_resources.py:2623(<lambda>)
      191    0.000    0.000    0.000    0.000 {built-in method search}
      250    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
        1    0.000    0.000    0.000    0.000 exceptions.py:3(<module>)
       85    0.000    0.000    0.002    0.000 posixpath.py:341(abspath)
       36    0.000    0.000    0.000    0.000 {posix.access}
        1    0.000    0.000    0.376    0.376 pkg_resources.py:673(subscribe)
       89    0.000    0.000    0.000    0.000 sre_parse.py:257(_escape)
       29    0.000    0.000    0.001    0.000 pkg_resources.py:1805(file_ns_handler)
      188    0.000    0.000    0.000    0.000 stat.py:40(S_ISDIR)
       51    0.000    0.000    0.000    0.000 sre_parse.py:225(_class_escape)
        6    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x10eb2af30}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        4    0.000    0.000    0.000    0.000 {dir}
      169    0.000    0.000    0.000    0.000 posixpath.py:51(isabs)
        1    0.000    0.000    0.475    0.475 xapiandb.py:73(createdb)
        3    0.000    0.000    0.000    0.000 sre_compile.py:258(_mk_bitmap)
      152    0.000    0.000    0.001    0.000 posixpath.py:95(splitext)
      152    0.000    0.000    0.002    0.000 pkg_resources.py:1108(safe_name)
       99    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.018    0.018 ssl.py:12(<module>)
        1    0.000    0.000    0.000    0.000 beautifullog.py:1(<module>)
        1    0.000    0.000    0.000    0.000 base64.py:3(<module>)
        9    0.000    0.000    0.001    0.000 argparse.py:1248(add_argument)
        3    0.000    0.000    0.001    0.000 gettext.py:421(find)
      101    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1559(ImpWrapper)
        2    0.000    0.000    0.000    0.000 {_curses.setupterm}
       36    0.000    0.000    0.009    0.000 sre_compile.py:480(_code)
        1    0.000    0.000    0.445    0.445 xapiandb.py:119(__init__)
        5    0.000    0.000    0.001    0.000 abc.py:86(__new__)
        1    0.000    0.000    0.221    0.221 pkg_resources.py:698(Environment)
        6    0.000    0.000    0.000    0.000 gettext.py:130(_expand_lang)
      386    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
       10    0.000    0.000    0.001    0.000 pkg_resources.py:1354(_extract_resource)
        5    0.000    0.000    0.000    0.000 {posix.getcwd}
       70    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
        1    0.000    0.000    0.000    0.000 event.py:2(<module>)
       40    0.000    0.000    0.002    0.000 pkg_resources.py:1653(find_distributions)
       36    0.000    0.000    0.000    0.000 {_sre.compile}
        9    0.000    0.000    0.000    0.000 argparse.py:1378(_get_optional_kwargs)
        1    0.000    0.000    0.000    0.000 argparse.py:1515(ArgumentParser)
      130    0.000    0.000    0.000    0.000 pkg_resources.py:1538(__init__)
        1    0.000    0.000    0.031    0.031 __init__.py:28(swig_import_helper)
      2/1    0.000    0.000   94.128   94.128 indexd.py:24(main)
        1    0.000    0.000    0.000    0.000 ascii.py:8(<module>)
      100    0.000    0.000    0.000    0.000 pkgutil.py:173(__init__)
      3/2    0.000    0.000    0.034    0.017 pkg_resources.py:1764(declare_namespace)
        1    0.000    0.000    0.001    0.001 {built-in method ParseFile}
       36    0.000    0.000    0.000    0.000 sre_parse.py:178(__init__)
        1    0.000    0.000    0.024    0.024 hub.py:308(__init__)
      312    0.000    0.000    0.000    0.000 {ord}
       25    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
        2    0.000    0.000   84.877   42.439 greenlet.py:321(run)
       72    0.000    0.000    0.000    0.000 sre_compile.py:474(isstring)
        3    0.000    0.000    0.001    0.000 argparse.py:1167(__init__)
        1    0.000    0.000    0.444    0.444 __init__.py:4289(__init__)
        1    0.000    0.000    0.001    0.001 xapiandb.py:199(load_config)
       70    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
        3    0.000    0.000    0.000    0.000 socket.py:225(__init__)
        2    0.000    0.000    0.000    0.000 {method 'get_data' of 'zipimport.zipimporter' objects}
      3/2    0.000    0.000    0.024    0.012 hub.py:239(_import)
        6    0.000    0.000    0.000    0.000 locale.py:334(normalize)
       10    0.000    0.000    0.000    0.000 {time.mktime}
       17    0.000    0.000    0.000    0.000 sre_parse.py:216(isname)
        1    0.000    0.000    0.000    0.000 timeout.py:14(<module>)
        1    0.000    0.000    0.000    0.000 hub.py:340(handle_error)
      111    0.000    0.000    0.000    0.000 sre_parse.py:134(__setitem__)
       76    0.000    0.000    0.000    0.000 pkg_resources.py:681(_added_new)
       20    0.000    0.000    0.004    0.000 pkg_resources.py:1827(normalize_path)
       10    0.000    0.000    0.000    0.000 pkg_resources.py:944(get_cache_path)
        2    0.000    0.000    0.000    0.000 greenlet.py:73(__init__)
       10    0.000    0.000    0.000    0.000 pkg_resources.py:1067(get_default_cache)
        1    0.000    0.000    0.000    0.000 argparse.py:1719(_parse_known_args)
        2    0.000    0.000    0.000    0.000 ConfigParser.py:224(__init__)
       34    0.000    0.000    0.000    0.000 argparse.py:1219(register)
       29    0.000    0.000    0.000    0.000 pkgutil.py:229(__init__)
        1    0.000    0.000    0.022    0.022 sysconfig.py:369(_init_posix)
       73    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
       14    0.000    0.000    0.000    0.000 pkg_resources.py:1846(yield_lines)
        2    0.000    0.000    0.445    0.222 xapiandb.py:29(get_db)
        9    0.000    0.000    0.000    0.000 argparse.py:1298(_add_action)
        1    0.000    0.000    0.000    0.000 util.py:3(<module>)
        1    0.000    0.000    0.000    0.000 beautifullog.py:26(__init__)
        1    0.000    0.000    0.000    0.000 os.py:35(_get_exports_list)
        1    0.000    0.000    0.000    0.000 sysconfig.py:10(<module>)
        1    0.000    0.000    0.000    0.000 {_xapian.WritableDatabase_swiginit}
        1    0.000    0.000    0.009    0.009 platform.py:10(<module>)
       38    0.000    0.000    0.020    0.001 re.py:188(compile)
       10    0.000    0.000    0.000    0.000 posixpath.py:249(expanduser)
        2    0.000    0.000    0.000    0.000 {method 'write' of 'file' objects}
        1    0.000    0.000    0.000    0.000 socket.py:179(_socketobject)
       13    0.000    0.000    0.000    0.000 posixpath.py:80(split)
       66    0.000    0.000    0.000    0.000 {setattr}
        1    0.000    0.000    0.000    0.000 event.py:54(wait)
        1    0.000    0.000    0.002    0.002 argparse.py:1533(__init__)
        9    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
       12    0.000    0.000    0.000    0.000 pkg_resources.py:1332(_parts)
       79    0.000    0.000    0.000    0.000 {imp.acquire_lock}
       10    0.000    0.000    0.001    0.000 pkg_resources.py:2205(from_filename)
        1    0.000    0.000    0.000    0.000 request.py:3(<module>)
       24    0.000    0.000    0.000    0.000 _weakrefset.py:58(__iter__)
       52    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {_xapian.new_Query}
        3    0.000    0.000    0.000    0.000 {posix.uname}
        1    0.000    0.000    0.000    0.000 baseserver.py:242(close)
      256    0.000    0.000    0.000    0.000 {chr}
        1    0.000    0.000    0.000    0.000 socket.py:308(close)
        1    0.000    0.000    0.001    0.001 argparse.py:1684(parse_known_args)
        1    0.000    0.000    0.001    0.001 xapiandb.py:51(_validate_config_file)
       36    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
        1    0.000    0.000    0.000    0.000 collections.py:46(OrderedDict)
        9    0.000    0.000    0.000    0.000 argparse.py:762(__init__)
       18    0.000    0.000    0.000    0.000 UserDict.py:58(get)
        1    0.000    0.000    0.475    0.475 server.py:154(handle_cmd_createdb)
        2    0.000    0.000    0.002    0.001 pkg_resources.py:1341(get_resource_filename)
        1    0.000    0.000    1.715    1.715 xapiandb.py:256(close)
        1    0.000    0.000    0.000    0.000 new.py:5(<module>)
       12    0.000    0.000    0.000    0.000 plistlib.py:409(handleBeginElement)
        2    0.000    0.000    0.000    0.000 xapiandb.py:48(_config_file_path)
      141    0.000    0.000    0.000    0.000 sre_compile.py:24(_identityfunction)
        9    0.000    0.000    0.024    0.003 hub.py:202(get_hub)
       27    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       65    0.000    0.000    0.000    0.000 pkg_resources.py:2533(cls)
       12    0.000    0.000    0.000    0.000 genericpath.py:26(isfile)
    34/20    0.000    0.000    0.000    0.000 {issubclass}
       79    0.000    0.000    0.000    0.000 {imp.release_lock}
        2    0.000    0.000    0.000    0.000 {_xapian.new_Stem}
        4    0.000    0.000    0.000    0.000 pkg_resources.py:1253(_setup_prefix)
        2    0.000    0.000    0.000    0.000 threading.py:180(__init__)
        9    0.000    0.000    0.000    0.000 argparse.py:1485(_add_action)
      144    0.000    0.000    0.000    0.000 {built-in method end}
       23    0.000    0.000    0.000    0.000 UserDict.py:18(__getitem__)
        1    0.000    0.000    0.000    0.000 argparse.py:146(HelpFormatter)
        3    0.000    0.000    0.022    0.007 sysconfig.py:484(get_config_vars)
        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
        4    0.000    0.000    0.000    0.000 threading.py:115(acquire)
       17    0.000    0.000    0.000    0.000 pkg_resources.py:1323(_zipinfo_name)
        2    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.028    0.028 pkg_resources.py:414(__init__)
        2    0.000    0.000    0.001    0.001 ConfigParser.py:302(readfp)
      206    0.000    0.000    0.000    0.000 {globals}
        7    0.000    0.000    0.000    0.000 argparse.py:804(__init__)
       76    0.000    0.000    0.000    0.000 sre_parse.py:210(isident)
        4    0.000    0.000    0.028    0.007 pkg_resources.py:1175(get_metadata)
        4    0.000    0.000    0.000    0.000 argparse.py:1766(take_action)
        4    0.000    0.000    0.000    0.000 argparse.py:1787(consume_optional)
        5    0.000    0.000    0.000    0.000 abc.py:89(<genexpr>)
        5    0.000    0.000    0.001    0.000 plistlib.py:451(end_key)
       22    0.000    0.000    0.000    0.000 argparse.py:1223(_registry_get)
        1    0.000    0.000    0.000    0.000 traceback.py:1(<module>)
        1    0.000    0.000    0.000    0.000 hub.py:352(print_exception)
        1    0.000    0.000    0.000    0.000 threading.py:426(__init__)
        2    0.000    0.000    0.028    0.014 pkg_resources.py:1287(_get)
      144    0.000    0.000    0.000    0.000 {built-in method start}
       10    0.000    0.000    0.001    0.000 {method 'encode' of 'unicode' objects}
        2    0.000    0.000    0.000    0.000 greenlet.py:196(spawn)
        4    0.000    0.000    0.000    0.000 argparse.py:2166(_get_values)
        4    0.000    0.000    0.000    0.000 {_curses.tparm}
       10    0.000    0.000    0.000    0.000 pkg_resources.py:29(_bypass_ensure_directory)
       21    0.000    0.000    0.000    0.000 _weakrefset.py:77(add)
        1    0.000    0.000    0.000    0.000 log.py:1(<module>)
        1    0.000    0.000    0.000    0.000 server.py:121(handle_cmd_setdb)
       11    0.000    0.000    0.000    0.000 _weakrefset.py:26(__exit__)
        4    0.000    0.000    0.000    0.000 __init__.py:49(normalize_encoding)
        1    0.000    0.000    0.000    0.000 baseserver.py:134(_do_read)
        1    0.000    0.000    0.001    0.001 warnings.py:45(filterwarnings)
        1    0.000    0.000    0.001    0.001 __init__.py:71(search_function)
        1    0.000    0.000    0.000    0.000 threading.py:414(Thread)
        1    0.000    0.000    0.024    0.024 baseserver.py:54(__init__)
       33    0.000    0.000    0.000    0.000 plistlib.py:420(handleData)
        1    0.000    0.000    0.000    0.000 baseserver.py:14(BaseServer)
       22    0.000    0.000    0.000    0.000 argparse.py:94(_callable)
        1    0.000    0.000    0.002    0.002 ConfigParser.py:223(RawConfigParser)
       15    0.000    0.000    0.000    0.000 posixpath.py:110(basename)
        2    0.000    0.000    0.000    0.000 {method 'accept' of '_socket.socket' objects}
        8    0.000    0.000    0.000    0.000 abc.py:105(register)
        7    0.000    0.000    0.001    0.000 pkg_resources.py:1436(_has)
        2    0.000    0.000    0.000    0.000 argparse.py:1464(__init__)
        1    0.000    0.000    0.000    0.000 dep_util.py:5(<module>)
        4    0.000    0.000    0.000    0.000 threading.py:135(release)
       10    0.000    0.000    0.001    0.000 plistlib.py:433(getData)
        1    0.000    0.000    0.000    0.000 __init__.py:5719(__init__)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:2052(Distribution)
       34    0.000    0.000    0.000    0.000 UserDict.py:70(__contains__)
        1    0.000    0.000    0.001    0.001 server.py:140(_tcp_listener)
        3    0.000    0.000    0.001    0.000 gettext.py:527(dgettext)
        1    0.000    0.000    0.000    0.000 hub.py:345(handle_system_error)
        1    0.000    0.000    0.000    0.000 traceback.py:110(print_exception)
        4    0.000    0.000    0.000    0.000 argparse.py:1986(_match_argument)
        1    0.000    0.000    0.000    0.000 collections.py:326(Counter)
        1    0.000    0.000    0.000    0.000 traceback.py:147(format_exception_only)
        1    0.000    0.000    0.024    0.024 core.py:1(__bootstrap__)
       33    0.000    0.000    0.000    0.000 pyexpat.c:441(CharacterData)
        9    0.000    0.000    0.000    0.000 argparse.py:1413(_pop_action_class)
        1    0.000    0.000    0.000    0.000 argparse.py:1022(_SubParsersAction)
        1    0.000    0.000    0.000    0.000 __init__.py:3616(Database)
        2    0.000    0.000    0.000    0.000 __init__.py:994(getLogger)
        1    0.000    0.000    0.000    0.000 {_xapian.new_TermGenerator}
        4    0.000    0.000    0.000    0.000 argparse.py:2215(_get_value)
        2    0.000    0.000    0.002    0.001 pkg_resources.py:879(resource_filename)
       20    0.000    0.000    0.000    0.000 {_sre.getlower}
        1    0.000    0.000    0.000    0.000 text_file.py:78(__init__)
       11    0.000    0.000    0.000    0.000 _weakrefset.py:20(__enter__)
       12    0.000    0.000    0.001    0.000 plistlib.py:415(handleEndElement)
        5    0.000    0.000    0.000    0.000 {method 'callback' of 'gevent.core.loop' objects}
      2/1    0.000    0.000   94.128   94.128 server.py:43(start)
        3    0.000    0.000    0.001    0.000 gettext.py:461(translation)
        4    0.000    0.000    0.028    0.007 pkg_resources.py:1180(get_metadata_lines)
        1    0.000    0.000    0.000    0.000 {method 'throw' of 'greenlet.greenlet' objects}
        1    0.000    0.000    0.000    0.000 event.py:117(AsyncResult)
        5    0.000    0.000    0.000    0.000 server.py:18(indexdb_set)
        2    0.000    0.000    0.000    0.000 timeout.py:86(__init__)
       20    0.000    0.000    0.000    0.000 pkg_resources.py:1489(__init__)
        2    0.000    0.000    0.000    0.000 timeout.py:105(start_new)
        1    0.000    0.000    0.000    0.000 greenlet.py:70(Greenlet)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:194(get_provider)
       41    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       11    0.000    0.000    0.000    0.000 {method 'split' of 'unicode' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:7498(_stem_init)
        1    0.000    0.000    0.000    0.000 text_file.py:5(<module>)
        2    0.000    0.000    0.000    0.000 _abcoll.py:371(values)
        9    0.000    0.000    0.000    0.000 argparse.py:1657(_add_action)
        1    0.000    0.000    0.000    0.000 hub.py:290(Hub)
        8    0.000    0.000    0.000    0.000 pkg_resources.py:1446(_eager_to_zip)
        1    0.000    0.000    0.024    0.024 event.py:20(__init__)
        9    0.000    0.000    0.000    0.000 argparse.py:1426(_check_conflict)
        1    0.000    0.000    0.000    0.000 threading.py:742(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:1092(__init__)
        1    0.000    0.000    0.099    0.099 plistlib.py:68(readPlist)
        4    0.000    0.000    0.000    0.000 pkg_resources.py:1659(find_in_zip)
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'unicode' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:243(AssertionError)
        4    0.000    0.000    0.000    0.000 hub.py:273(config)
        1    0.000    0.000    0.000    0.000 __init__.py:201(LogicError)
        2    0.000    0.000    0.000    0.000 {_curses.tigetstr}
        1    0.000    0.000    0.000    0.000 __init__.py:2098(MSet)
        1    0.000    0.000    0.000    0.000 __init__.py:2753(Enquire)
        2    0.000    0.000    0.000    0.000 __init__.py:6957(_query_init)
        2    0.000    0.000    0.000    0.000 event.py:37(set)
       12    0.000    0.000    0.001    0.000 pyexpat.c:618(EndElement)
        2    0.000    0.000    0.000    0.000 __init__.py:1036(_fixupParents)
        1    0.000    0.000    0.000    0.000 server.py:47(Connection)
        2    0.000    0.000    0.000    0.000 greenlet.py:303(_report_result)
        4    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}
        2    0.000    0.000    0.000    0.000 greenlet.py:184(start)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:2587(_initialize)
        1    0.000    0.000    0.000    0.000 {_xapian.SwigPyIterator_swigregister}
        1    0.000    0.000    0.016    0.016 pkgutil.py:235(load_module)
        2    0.000    0.000    0.000    0.000 argparse.py:1288(add_argument_group)
        9    0.000    0.000    0.000    0.000 functools.py:39(wraps)
        4    0.000    0.000    0.000    0.000 argparse.py:2122(_get_nargs_pattern)
        1    0.000    0.000    0.000    0.000 __init__.py:5290(QueryParser)
        1    0.000    0.000    0.000    0.000 __init__.py:1241(Document)
        2    0.000    0.000    0.001    0.000 pkg_resources.py:1410(_get_eager_resources)
        1    0.000    0.000    0.000    0.000 collections.py:20(_recursive_repr)
        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:4951(Query)
       12    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {posix.putenv}
        1    0.000    0.000    0.000    0.000 wrapper.py:8(<module>)
       15    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 pyexpat.c:566(StartElement)
        1    0.000    0.000    0.000    0.000 {method 'getsockname' of '_socket.socket' objects}
        4    0.000    0.000    0.000    0.000 pkg_resources.py:44(_declare_state)
        2    0.000    0.000    0.000    0.000 __init__.py:5669(__init__)
        1    0.000    0.000    0.000    0.000 sysconfig.py:45(_python_build)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1318(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:365(__init__)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:411(WorkingSet)
        1    0.000    0.000    0.025    0.025 server.py:37(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:799(SerialisationError)
        6    0.000    0.000    0.000    0.000 {method 'acquire' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 baseserver.py:119(stop_accepting)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1546(__init__)
        7    0.000    0.000    0.000    0.000 {method 'io' of 'gevent.core.loop' objects}
        2    0.000    0.000    0.000    0.000 server.py:84(do_read)
        1    0.000    0.000    0.221    0.221 pkg_resources.py:83(get_supported_platform)
        1    0.000    0.000    0.000    0.000 atexit.py:6(<module>)
        3    0.000    0.000    0.001    0.000 gettext.py:565(gettext)
       11    0.000    0.000    0.000    0.000 _weakrefset.py:16(__init__)
        1    0.000    0.000    0.000    0.000 server.py:62(set_listener)
        1    0.000    0.000    0.000    0.000 ssl.py:61(SSLSocket)
        3    0.000    0.000    0.000    0.000 argparse.py:1417(_get_handler)
        4    0.000    0.000    0.000    0.000 __init__.py:210(_acquireLock)
        3    0.000    0.000    0.000    0.000 {method 'setblocking' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 timeout.py:33(Timeout)
        2    0.000    0.000    0.000    0.000 threading.py:100(__init__)
       13    0.000    0.000    0.000    0.000 {method 'readline' of '_io.StringIO' objects}
        2    0.000    0.000    0.000    0.000 {method 'timer' of 'gevent.core.loop' objects}
        1    0.000    0.000    0.000    0.000 ssl.py:83(SSLSocket)
       10    0.000    0.000    0.000    0.000 stat.py:49(S_ISREG)
        4    0.000    0.000    0.000    0.000 server.py:27(conn_writable)
        1    0.000    0.000    0.000    0.000 __init__.py:5708(TermGenerator)
        1    0.000    0.000    0.000    0.000 __init__.py:4282(WritableDatabase)
        1    0.000    0.000    0.000    0.000 __init__.py:104(SwigPyIterator)
        1    0.000    0.000    0.000    0.000 __init__.py:565(DatabaseVersionError)
        1    0.000    0.000    0.000    0.000 baseserver.py:113(start_accepting)
        1    0.000    0.000    0.000    0.000 plistlib.py:393(PlistParser)
        9    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:312(InvalidOperationError)
        1    0.000    0.000    0.024    0.024 server.py:40(__init__)
        2    0.000    0.000    0.000    0.000 timeout.py:94(start)
        1    0.000    0.000    0.000    0.000 text_file.py:12(TextFile)
        1    0.000    0.000    0.000    0.000 greenlet.py:279(join)
        1    0.000    0.000    0.000    0.000 __init__.py:2509(ESet)
        1    0.000    0.000    0.000    0.000 {_curses.tigetnum}
        1    0.000    0.000    0.000    0.000 socket.py:235(_fileobject)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1156(__init__)
       11    0.000    0.000    0.000    0.000 {method 'lower' of 'unicode' objects}
        2    0.000    0.000    0.000    0.000 timeout.py:130(cancel)
        5    0.000    0.000    0.000    0.000 re.py:134(match)
        1    0.000    0.000    0.000    0.000 threading.py:178(_Condition)
        1    0.000    0.000    0.000    0.000 codecs.py:77(__new__)
        1    0.000    0.000    0.000    0.000 __init__.py:1586(info)
        1    0.000    0.000    0.000    0.000 __init__.py:1597(PostingSource)
        1    0.000    0.000    0.000    0.000 __init__.py:343(UnimplementedError)
        1    0.000    0.000    0.000    0.000 server.py:84(do_handshake)
        1    0.000    0.000    0.000    0.000 ascii.py:41(getregentry)
        1    0.000    0.000    0.000    0.000 sysconfig.py:99(get_python_lib)
        1    0.000    0.000    0.000    0.000 __init__.py:468(DatabaseLockError)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1249(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:221(RuntimeError)
        1    0.000    0.000    0.000    0.000 __init__.py:641(Handler)
        1    0.000    0.000    0.679    0.679 _util.py:1(<module>)
        3    0.000    0.000    0.000    0.000 __init__.py:390(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:639(FeatureUnavailableError)
        1    0.000    0.000    0.000    0.000 traceback.py:202(_format_final_exc_line)
        6    0.000    0.000    0.000    0.000 __init__.py:182(_checkLevel)
        1    0.000    0.000    0.000    0.000 <string>:1(listen)
        1    0.000    0.000    0.000    0.000 socket.py:606(BlockingResolver)
        1    0.000    0.000    0.000    0.000 __init__.py:923(PostingIterator)
        1    0.000    0.000    0.001    0.001 baseserver.py:228(start)
        1    0.000    0.000    0.000    0.000 __init__.py:812(__init__)
        1    0.000    0.000    0.000    0.000 traceback.py:211(_some_str)
        1    0.000    0.000    0.000    0.000 __init__.py:877(PositionIterator)
        1    0.000    0.000    0.000    0.000 __init__.py:1077(Logger)
        1    0.000    0.000    0.000    0.000 __init__.py:830(RangeError)
        3    0.000    0.000    0.000    0.000 __init__.py:1531(getLogger)
        1    0.000    0.000    0.000    0.000 __init__.py:674(InternalError)
        1    0.000    0.000    0.000    0.000 __init__.py:490(BufferingFormatter)
        1    0.000    0.000    0.000    0.000 __init__.py:2374(MSetIterator)
        1    0.000    0.000    0.000    0.000 __init__.py:499(DatabaseModifiedError)
       11    0.000    0.000    0.000    0.000 _weakrefset.py:52(_commit_removals)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1236(_get)
        1    0.000    0.000    0.000    0.000 threading.py:711(_Timer)
        8    0.000    0.000    0.000    0.000 argparse.py:2021(_parse_optional)
        1    0.000    0.000    0.000    0.000 argparse.py:980(__init__)
        1    0.000    0.000    0.001    0.001 server.py:69(init_socket)
        1    0.000    0.000    0.000    0.000 __init__.py:375(DatabaseError)
        1    0.000    0.000    0.000    0.000 __init__.py:1023(TermIterator)
        1    0.000    0.000    0.000    0.000 threading.py:375(set)
        1    0.000    0.000    0.000    0.000 __init__.py:2637(RSet)
        1    0.000    0.000    0.000    0.000 __init__.py:534(DatabaseOpeningError)
        1    0.000    0.000    0.000    0.000 __init__.py:768(QueryParserError)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:862(ResourceManager)
        1    0.000    0.000    0.000    0.000 __init__.py:3164(Registry)
        1    0.000    0.000    0.000    0.000 __init__.py:607(DocNotFoundError)
        1    0.000    0.000    0.000    0.000 server.py:12(StreamServer)
        6    0.000    0.000    0.000    0.000 threading.py:58(__init__)
        2    0.000    0.000    0.000    0.000 threading.py:95(RLock)
        1    0.000    0.000    0.000    0.000 __init__.py:3405(BM25Weight)
        1    0.000    0.000    0.000    0.000 hub.py:137(signal)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:112(Error)
        2    0.000    0.000    0.000    0.000 threading.py:175(Condition)
        1    0.000    0.000    0.000    0.000 __init__.py:6109(Compactor)
        5    0.000    0.000    0.000    0.000 plistlib.py:469(end_string)
        1    0.000    0.000    0.000    0.000 argparse.py:1864(consume_positionals)
        1    0.000    0.000    0.000    0.000 {_xapian.RSet_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:1365(LoggerAdapter)
        1    0.000    0.000    0.000    0.000 __init__.py:2072(FixedWeightPostingSource)
        1    0.000    0.000    0.000    0.000 __init__.py:631(_addHandlerRef)
        1    0.000    0.000    0.000    0.000 __init__.py:3452(MatchSpy)
        1    0.000    0.000    0.000    0.000 {pyexpat.ParserCreate}
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1929(EntryPoint)
        1    0.000    0.000    0.000    0.000 {_xapian.NetworkError_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:3288(Weight)
        1    0.000    0.000    0.000    0.000 weakref.py:47(__init__)
        1    0.000    0.000    0.000    0.000 event.py:87(rawlink)
        1    0.000    0.000    0.000    0.000 baseserver.py:261(stop)
       22    0.000    0.000    0.000    0.000 {max}
        1    0.000    0.000    0.000    0.000 __init__.py:1357(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:650(__init__)
        1    0.000    0.000    0.000    0.000 event.py:100(unlink)
        1    0.000    0.000    0.000    0.000 __init__.py:736(NetworkTimeoutError)
        2    0.000    0.000    0.000    0.000 __init__.py:5038(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:705(NetworkError)
       21    0.000    0.000    0.000    0.000 {method 'strip' of 'unicode' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1120(ValueIterator)
        3    0.000    0.000    0.000    0.000 string.py:511(replace)
        1    0.000    0.000    0.000    0.000 __init__.py:2002(ValueMapPostingSource)
        1    0.000    0.000    0.000    0.000 hub.py:505(Waiter)
        1    0.000    0.000    0.000    0.000 __init__.py:3534(ValueCountMatchSpy)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1149(NullProvider)
        4    0.000    0.000    0.000    0.000 __init__.py:574(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:569(Filterer)
        1    0.000    0.000    0.000    0.000 greenlet.py:338(rawlink)
        1    0.000    0.000    0.000    0.000 threading.py:298(_Semaphore)
        1    0.000    0.000    0.000    0.000 __init__.py:137(Error)
        1    0.000    0.000    0.000    0.000 baseserver.py:72(set_listener)
        1    0.000    0.000    0.000    0.000 text_file.py:124(close)
        1    0.000    0.000    0.000    0.000 traceback.py:12(_print)
        1    0.000    0.000    0.000    0.000 request.py:26(get_string)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1313(ZipProvider)
        1    0.000    0.000    0.000    0.000 __init__.py:406(DatabaseCorruptError)
        1    0.000    0.000    0.000    0.000 __init__.py:3419(TradWeight)
        1    0.000    0.000    0.000    0.000 __init__.py:979(Manager)
        1    0.000    0.000    0.000    0.000 xapiandb.py:44(_validate_dbname)
        2    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
        2    0.000    0.000    0.000    0.000 greenlet.py:104(ready)
        2    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {imp.new_module}
        1    0.000    0.000    0.000    0.000 plistlib.py:444(begin_dict)
        5    0.000    0.000    0.000    0.000 {thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 {method 'listen' of '_socket.socket' objects}
       10    0.000    0.000    0.000    0.000 pkg_resources.py:1492(has_metadata)
        1    0.000    0.000    0.000    0.000 <string>:1(setsockopt)
        1    0.000    0.000    0.000    0.000 plistlib.py:151(DumbXMLWriter)
        1    0.000    0.000    0.000    0.000 threading.py:220(_is_owned)
        1    0.000    0.000    0.000    0.000 __init__.py:1897(ValuePostingSource)
        1    0.000    0.000    0.000    0.000 __init__.py:1262(addHandler)
        1    0.000    0.000    0.000    0.000 {method 'setsockopt' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:437(DatabaseCreateError)
        1    0.000    0.000    0.000    0.000 __init__.py:2596(ESetIterator)
        1    0.000    0.000    0.000    0.000 event.py:11(Event)
        6    0.000    0.000    0.000    0.000 plistlib.py:423(addObject)
        1    0.000    0.000    0.000    0.000 __init__.py:6618(TermIter)
        1    0.000    0.000    0.000    0.000 __init__.py:6500(TermListItem)
        1    0.000    0.000    0.000    0.000 __init__.py:2732(ExpandDecider)
        4    0.000    0.000    0.000    0.000 argparse.py:833(__call__)
       10    0.000    0.000    0.000    0.000 {method 'isspace' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'find_module' of 'zipimport.zipimporter' objects}
        1    0.000    0.000    0.000    0.000 exceptions.py:13(AWIPErrorWithCode)
        1    0.000    0.000    0.000    0.000 __init__.py:3386(BoolWeight)
        1    0.000    0.000    0.000    0.000 baseserver.py:295(_parse_address)
        1    0.000    0.000    0.000    0.000 __init__.py:5937(KeyMaker)
        1    0.000    0.000    0.001    0.001 <string>:1(bind)
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        1    0.000    0.000    0.000    0.000 argparse.py:862(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:932(PlaceHolder)
        1    0.000    0.000    0.001    0.001 server.py:78(get_listener)
        4    0.000    0.000    0.000    0.000 sysconfig.py:53(get_python_version)
        1    0.000    0.000    0.000    0.000 log.py:14(Log)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1449(_resource_to_zip)
        1    0.000    0.000    0.000    0.000 __init__.py:5069(Stopper)
        1    0.000    0.000    0.000    0.000 re.py:169(findall)
        1    0.000    0.000    0.000    0.000 sysconfig.py:216(get_makefile_filename)
        6    0.000    0.000    0.000    0.000 {locals}
        1    0.000    0.000    0.000    0.000 __init__.py:5125(ValueRangeProcessor)
        1    0.000    0.000    0.000    0.000 argparse.py:839(__init__)
        1    0.000    0.000    0.000    0.000 server.py:125(handle_cmd_setmode)
        1    0.000    0.000    0.000    0.000 __init__.py:1968(DecreasingValueWeightPostingSource)
        1    0.000    0.000    0.000    0.000 sysconfig.py:61(get_python_inc)
        2    0.000    0.000    0.001    0.000 re.py:139(search)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1272(DefaultProvider)
        1    0.000    0.000    0.000    0.000 <string>:1(getsockname)
        1    0.000    0.000    0.000    0.000 __init__.py:5958(MultiValueKeyMaker)
        4    0.000    0.000    0.000    0.000 sre_parse.py:128(__delitem__)
        1    0.000    0.000    0.000    0.000 __init__.py:5234(NumberValueRangeProcessor)
        1    0.000    0.000    0.000    0.000 __init__.py:7124(PostingItem)
        1    0.000    0.000    0.000    0.000 __init__.py:1928(ValueWeightPostingSource)
        1    0.000    0.000    0.000    0.000 __init__.py:2711(MatchDecider)
        1    0.000    0.000    0.000    0.000 hub.py:280(resolver_config)
        1    0.000    0.000    0.000    0.000 threading.py:271(notify)
        1    0.000    0.000    0.000    0.000 __init__.py:5632(StemImplementation)
        1    0.000    0.000    0.000    0.000 threading.py:98(_RLock)
        9    0.000    0.000    0.000    0.000 threading.py:63(_note)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:329(IMetadataProvider)
        2    0.000    0.000    0.000    0.000 timeout.py:125(pending)
        3    0.000    0.000    0.000    0.000 {method 'start' of 'gevent.core.callback' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:5146(StringValueRangeProcessor)
        1    0.000    0.000    0.000    0.000 __init__.py:5997(Sorter)
        1    0.000    0.000    0.000    0.000 {built-in method findall}
        1    0.000    0.000    0.000    0.000 xapiandb.py:24(set_scws_data)
        1    0.000    0.000    0.000    0.000 xapiandb.py:114(XapianDB)
        1    0.000    0.000    0.000    0.000 __init__.py:6008(MultiValueSorter)
        1    0.000    0.000    0.000    0.000 {_xapian.RuntimeError_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:6051(ValueSetMatchDecider)
        1    0.000    0.000    0.000    0.000 __init__.py:5663(Stem)
        1    0.000    0.000    0.000    0.000 __init__.py:6911(wrapper)
        1    0.000    0.000    0.000    0.000 __init__.py:5099(SimpleStopper)
        1    0.000    0.000    0.000    0.000 __init__.py:5177(DateValueRangeProcessor)
        1    0.000    0.000    0.000    0.000 __init__.py:679(createLock)
        1    0.000    0.000    0.000    0.000 argparse.py:1142(Namespace)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:2462(Requirement)
        1    0.000    0.000    0.000    0.000 {_xapian.QueryParserError_swigregister}
        1    0.000    0.000    0.000    0.000 argparse.py:931(_AppendConstAction)
        1    0.000    0.000    0.000    0.000 {sorted}
        1    0.000    0.000    0.000    0.000 threading.py:358(Event)
        1    0.000    0.000    0.000    0.000 platform.py:365(_popen)
        1    0.000    0.000    0.000    0.000 argparse.py:2005(_match_arguments_partial)
        1    0.000    0.000    0.000    0.000 string.py:220(lower)
        1    0.000    0.000    0.000    0.000 {signal.signal}
        1    0.000    0.000    0.000    0.000 text_file.py:115(open)
        1    0.000    0.000    0.000    0.000 argparse.py:957(_CountAction)
        2    0.000    0.000    0.000    0.000 hub.py:389(cancel_wait)
        1    0.000    0.000    0.024    0.024 core.py:1(<module>)
        1    0.000    0.000    0.000    0.000 greenlet.py:13(SpawnedLink)
       10    0.000    0.000    0.000    0.000 {method 'isspace' of 'unicode' objects}
        1    0.000    0.000    0.000    0.000 plistlib.py:331(Plist)
        1    0.000    0.000    0.000    0.000 argparse.py:1165(_ActionsContainer)
        2    0.000    0.000    0.000    0.000 {_socket.getdefaulttimeout}
        1    0.000    0.000    0.000    0.000 server.py:99(DatagramServer)
       21    0.000    0.000    0.000    0.000 posixpath.py:43(normcase)
        1    0.000    0.000    0.000    0.000 argparse.py:1669(_get_positional_actions)
       12    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
        4    0.000    0.000    0.000    0.000 __init__.py:219(_releaseLock)
        1    0.000    0.000    0.000    0.000 pprint.py:81(PrettyPrinter)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1838(_set_parent_ns)
        1    0.000    0.000    0.000    0.000 baseserver.py:224(started)
       12    0.000    0.000    0.000    0.000 {thread.get_ident}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:548(ConfigParser)
        1    0.000    0.000    0.000    0.000 request.py:5(Request)
        1    0.000    0.000    0.000    0.000 plistlib.py:448(end_dict)
        1    0.000    0.000    0.000    0.000 __init__.py:6307(MSetItem)
        1    0.000    0.000    0.000    0.000 __init__.py:346(Formatter)
        1    0.000    0.000    0.000    0.000 threading.py:509(_set_ident)
        1    0.000    0.000    0.000    0.000 baseserver.py:315(parse_address)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:370(IResourceProvider)
        1    0.000    0.000    0.112    0.112 platform.py:791(mac_ver)
        1    0.000    0.000    0.000    0.000 argparse.py:997(_VersionAction)
        1    0.000    0.000    0.000    0.000 xapiandb.py:85(ZhTermGenerator)
        1    0.000    0.000    0.000    0.000 __init__.py:702(setLevel)
        1    0.000    0.000    0.000    0.000 indexd.py:21(log_level)
        1    0.000    0.000    0.000    0.000 sysconfig.py:199(get_config_h_filename)
        1    0.000    0.000    0.000    0.000 __init__.py:9(<module>)
        2    0.000    0.000    0.000    0.000 baseserver.py:169(full)
        1    0.000    0.000    0.000    0.000 {_xapian.SerialisationError_swigregister}
        1    0.000    0.000    0.000    0.000 baseserver.py:82(set_spawn)
        1    0.000    0.000    0.000    0.000 log.py:16(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:7457(wrapper)
        1    0.000    0.000    0.000    0.000 socket.py:167(_closedsocket)
        1    0.000    0.000    0.000    0.000 {_xapian.TermGenerator_swiginit}
        1    0.000    0.000    0.000    0.000 argparse.py:1149(__init__)
        1    0.000    0.000    0.000    0.000 atexit.py:37(register)
        5    0.000    0.000    0.000    0.000 {method 'release' of 'thread.lock' objects}
       11    0.000    0.000    0.000    0.000 {method '__subclasses__' of 'type' objects}
        2    0.000    0.000    0.000    0.000 {_xapian.Query_swiginit}
        1    0.000    0.000    0.000    0.000 beautifullog.py:25(TornadoLogFormatter)
        1    0.000    0.000    0.000    0.000 {_xapian.Document_swigregister}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:644(SafeConfigParser)
        1    0.000    0.000    0.000    0.000 {_xapian.ValueWeightPostingSource_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseVersionError_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:7184(PostingIter)
        1    0.000    0.000    0.000    0.000 __init__.py:230(LogRecord)
        1    0.000    0.000    0.000    0.000 {_xapian.KeyMaker_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:872(FileHandler)
        1    0.000    0.000    0.000    0.000 {_xapian.UnimplementedError_swigregister}
        1    0.000    0.000    0.000    0.000 io.py:78(IOBase)
        1    0.000    0.000    0.000    0.000 plistlib.py:230(PlistWriter)
        1    0.000    0.000    0.000    0.000 {_xapian.TermIterator_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:532(Filter)
        4    0.000    0.000    0.000    0.000 argparse.py:2240(_check_value)
        1    0.000    0.000    0.000    0.000 __init__.py:6434(ESetItem)
        4    0.000    0.000    0.000    0.000 {method 'translate' of 'str' objects}
        3    0.000    0.000    0.000    0.000 pkg_resources.py:185(register_loader_type)
        1    0.000    0.000    0.000    0.000 {_xapian.Database_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.NetworkTimeoutError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.ValueCountMatchSpy_swigregister}
        2    0.000    0.000    0.000    0.000 {method 'stop' of 'gevent.core.timer' objects}
        1    0.000    0.000    0.000    0.000 {_xapian.Query_swigregister}
        1    0.000    0.000    0.000    0.000 baseserver.py:127(do_handle)
        1    0.000    0.000    0.000    0.000 {_xapian.MSetIterator_swigregister}
        5    0.000    0.000    0.000    0.000 _abcoll.py:97(__subclasshook__)
        1    0.000    0.000    0.000    0.000 __init__.py:984(__init__)
        4    0.000    0.000    0.000    0.000 {method 'iteritems' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseCreateError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.PostingIterator_swigregister}
        1    0.000    0.000    0.000    0.000 threading.py:289(notifyAll)
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseModifiedError_swigregister}
        1    0.000    0.000    0.000    0.000 warnings.py:14(warnpy3k)
        1    0.000    0.000    0.000    0.000 socket.py:499(setblocking)
        1    0.000    0.000    0.000    0.000 __init__.py:153(getLevelName)
        1    0.000    0.000    0.000    0.000 {_xapian.Stem_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.WritableDatabase_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:938(__init__)
        1    0.000    0.000    0.000    0.000 {_xapian.Compactor_swigregister}
        1    0.000    0.000    0.000    0.000 plistlib.py:395(__init__)
        1    0.000    0.000    0.000    0.000 constants.py:3(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:7396(ValueStreamIter)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1297(EmptyProvider)
        1    0.000    0.000    0.000    0.000 {_xapian.MatchDecider_swigregister}
        1    0.000    0.000    0.000    0.000 threading.py:361(_Event)
        1    0.000    0.000    0.000    0.000 __init__.py:6932(wrapper)
        1    0.000    0.000    0.000    0.000 hub.py:187(get_hub_class)
        1    0.000    0.000    0.000    0.000 {_xapian.InvalidOperationError_swigregister}
        1    0.000    0.000    0.000    0.000 socket.py:208(_closedsocket)
        1    0.000    0.000    0.000    0.000 threading.py:780(_DummyThread)
        1    0.000    0.000    0.000    0.000 {_xapian.InvalidArgumentError_swigregister}
        1    0.000    0.000    0.000    0.000 errors.py:13(DistutilsError)
        1    0.000    0.000    0.000    0.000 {_xapian.SimpleStopper_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.AssertionError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.InternalError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.BM25Weight_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:1104(setLevel)
        1    0.000    0.000    0.000    0.000 {_xapian.MultiValueKeyMaker_swigregister}
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {_xapian.TermGenerator_set_stemmer}
        1    0.000    0.000    0.001    0.001 argparse.py:1677(parse_args)
        1    0.000    0.000    0.000    0.000 plistlib.py:365(Data)
        1    0.000    0.000    0.000    0.000 os.py:510(getenv)
        1    0.000    0.000    0.000    0.000 __init__.py:8(<module>)
        1    0.000    0.000    0.000    0.000 {_xapian.BoolWeight_swigregister}
        1    0.000    0.000    0.000    0.000 pkg_resources.py:165(ResolutionError)
        1    0.000    0.000    0.000    0.000 __init__.py:1649(NullHandler)
        1    0.000    0.000    0.000    0.000 baseserver.py:101(set_handle)
        6    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:146(DuplicateSectionError)
        1    0.000    0.000    0.000    0.000 {_xapian.ESetIterator_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.DateValueRangeProcessor_swigregister}
        1    0.000    0.000    0.000    0.000 <string>:1(fileno)
        1    0.000    0.000    0.000    0.000 {_xapian.TermGenerator_swigregister}
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1477(FileMetadata)
        1    0.000    0.000    0.000    0.000 argparse.py:702(ArgumentTypeError)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1305(__init__)
        1    0.000    0.000    0.000    0.000 ascii.py:13(Codec)
        1    0.000    0.000    0.000    0.000 {_xapian.ValueIterator_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.ValueSetMatchDecider_swigregister}
        1    0.000    0.000    0.000    0.000 errors.py:33(DistutilsFileError)
        1    0.000    0.000    0.000    0.000 xapiandb.py:20(set_dbdir)
        4    0.000    0.000    0.000    0.000 {method 'fileno' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 errors.py:46(DistutilsSetupError)
        1    0.000    0.000    0.000    0.000 {_xapian.DocNotFoundError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.Error_swigregister}
        1    0.000    0.000    0.000    0.000 {method 'find_module' of 'imp.NullImporter' objects}
        1    0.000    0.000    0.000    0.000 {_xapian.MultiValueSorter_swigregister}
        1    0.000    0.000    0.000    0.000 exceptions.py:38(AWIPClientError)
        1    0.000    0.000    0.000    0.000 {_xapian.StringValueRangeProcessor_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.MatchSpy_swigregister}
        1    0.000    0.000    0.000    0.000 argparse.py:194(_Section)
        1    0.000    0.000    0.000    0.000 threading.py:740(_MainThread)
        1    0.000    0.000    0.000    0.000 argparse.py:711(Action)
        1    0.000    0.000    0.000    0.000 {_xapian.FeatureUnavailableError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.NumberValueRangeProcessor_swigregister}
        3    0.000    0.000    0.000    0.000 pkg_resources.py:1726(register_namespace_handler)
        1    0.000    0.000    0.000    0.000 {_xapian.ValueRangeProcessor_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.ValuePostingSource_swigregister}
        1    0.000    0.000    0.000    0.000 argparse.py:1495(_MutuallyExclusiveGroup)
        1    0.000    0.000    0.000    0.000 {_xapian.DecreasingValueWeightPostingSource_swigregister}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:153(NoOptionError)
        1    0.000    0.000    0.000    0.000 __init__.py:1351(RootLogger)
        1    0.000    0.000    0.000    0.000 argparse.py:648(ArgumentDefaultsHelpFormatter)
        2    0.000    0.000    0.000    0.000 pkg_resources.py:1682(find_nothing)
        1    0.000    0.000    0.000    0.000 io.py:87(TextIOBase)
        1    0.000    0.000    0.000    0.000 ascii.py:28(StreamWriter)
        1    0.000    0.000    0.000    0.000 threading.py:346(_BoundedSemaphore)
        1    0.000    0.000    0.000    0.000 errors.py:87(UnknownFileError)
        1    0.000    0.000    0.000    0.000 __init__.py:749(setFormatter)
        1    0.000    0.000    0.000    0.000 errors.py:66(DistutilsByteCompileError)
        1    0.000    0.000    0.000    0.000 __init__.py:7273(PositionIter)
        1    0.000    0.000    0.000    0.000 exceptions.py:56(AWIPServerError)
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseError_swigregister}
        1    0.000    0.000    0.000    0.000 UserDict.py:4(__init__)
        1    0.000    0.000    0.000    0.000 exceptions.py:5(AWIPError)
        1    0.000    0.000    0.000    0.000 errors.py:73(PreprocessError)
        8    0.000    0.000    0.000    0.000 {method '__subclasshook__' of 'object' objects}
        1    0.000    0.000    0.000    0.000 argparse.py:111(_AttributeHolder)
        1    0.000    0.000    0.000    0.000 {_xapian.ESet_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.ExpandDecider_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.ValueMapPostingSource_swigregister}
        1    0.000    0.000    0.000    0.000 argparse.py:1024(_ChoicesPseudoAction)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1518(PathMetadata)
        1    0.000    0.000    0.000    0.000 {_xapian.Sorter_swigregister}
        1    0.000    0.000    0.000    0.000 argparse.py:860(_StoreTrueAction)
        1    0.000    0.000    0.000    0.000 threading.py:56(_Verbose)
        2    0.000    0.000    0.000    0.000 {callable}
        2    0.000    0.000    0.000    0.000 {method 'update' of 'set' objects}
        1    0.000    0.000    0.000    0.000 argparse.py:894(_AppendAction)
        1    0.000    0.000    0.000    0.000 util.py:52(CasedConfigParser)
        1    0.000    0.000    0.000    0.000 server.py:36(IndexServer)
        1    0.000    0.000    0.000    0.000 pkgutil.py:249(_reopen)
        2    0.000    0.000    0.000    0.000 argparse.py:1579(identity)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:169(VersionConflict)
        1    0.000    0.000    0.000    0.000 greenlet.py:46(SuccessSpawnedLink)
        2    0.000    0.000    0.000    0.000 {_xapian.Stem_swiginit}
        1    0.000    0.000    0.000    0.000 ConfigParser.py:170(InterpolationMissingOptionError)
        1    0.000    0.000    0.000    0.000 {_xapian.StemImplementation_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.Registry_swigregister}
        1    0.000    0.000    0.000    0.000 {zip}
        1    0.000    0.000    0.000    0.000 pkg_resources.py:866(__init__)
        1    0.000    0.000    0.000    0.000 {_xapian.LogicError_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:805(StreamHandler)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:175(UnknownExtra)
        1    0.000    0.000    0.000    0.000 errors.py:50(DistutilsPlatformError)
        1    0.000    0.000    0.000    0.000 errors.py:20(DistutilsClassError)
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseLockError_swigregister}
        3    0.000    0.000    0.000    0.000 pkg_resources.py:1643(register_finder)
        1    0.000    0.000    0.000    0.000 errors.py:83(LinkError)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:139(NoSectionError)
        1    0.000    0.000    0.000    0.000 {_xapian.Weight_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:7334(ValueIter)
        1    0.000    0.000    0.000    0.000 exceptions.py:41(AWIPHandshakeFailed)
        1    0.000    0.000    0.000    0.000 errors.py:29(DistutilsArgError)
        1    0.000    0.000    0.000    0.000 {iter}
        1    0.000    0.000    0.000    0.000 hub.py:630(_NONE)
        1    0.000    0.000    0.000    0.000 hub.py:501(LoopExit)
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseOpeningError_swigregister}
        1    0.000    0.000    0.000    0.000 errors.py:26(DistutilsGetoptError)
        1    0.000    0.000    0.000    0.000 ascii.py:20(IncrementalEncoder)
        1    0.000    0.000    0.000    0.000 plistlib.py:322(Dict)
        1    0.000    0.000    0.000    0.000 ascii.py:34(StreamConverter)
        1    0.000    0.000    0.000    0.000 {_xapian.PositionIterator_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.MSet_swigregister}
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1543(EggMetadata)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:844(ExtractionError)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1580(ImpLoader)
        1    0.000    0.000    0.000    0.000 {_xapian.FixedWeightPostingSource_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.RangeError_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:6362(MSetIter)
        1    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 argparse.py:802(_StoreAction)
        1    0.000    0.000    0.000    0.000 argparse.py:1099(FileType)
        1    0.000    0.000    0.000    0.000 {_xapian.QueryParser_swigregister}
        1    0.000    0.000    0.000    0.000 errors.py:55(DistutilsExecError)
        1    0.000    0.000    0.000    0.000 plistlib.py:291(_InternalDict)
        1    0.000    0.000    0.000    0.000 {_xapian.DatabaseCorruptError_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.TradWeight_swigregister}
        1    0.000    0.000    0.000    0.000 {_xapian.Stopper_swigregister}
        1    0.000    0.000    0.000    0.000 __init__.py:7318(ValueItem)
        2    0.000    0.000    0.000    0.000 {method 'stop' of 'gevent.core.callback' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:6449(ESetIter)
        1    0.000    0.000    0.000    0.000 argparse.py:877(_StoreFalseAction)
        1    0.000    0.000    0.000    0.000 {_xapian.Enquire_swigregister}
        1    0.000    0.000    0.000    0.000 errors.py:16(DistutilsModuleError)
        7    0.000    0.000    0.000    0.000 {method 'rstrip' of 'unicode' objects}
        1    0.000    0.000    0.000    0.000 event.py:47(clear)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:1246(EggProvider)
        1    0.000    0.000    0.000    0.000 __init__.py:945(append)
        1    0.000    0.000    0.000    0.000 {_xapian.PostingSource_swigregister}
        1    0.000    0.000    0.000    0.000 argparse.py:637(RawTextHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:626(RawDescriptionHelpFormatter)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:210(MissingSectionHeaderError)
        1    0.000    0.000    0.000    0.000 exceptions.py:54(AWIPRequestInvalid)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:198(ParsingError)
        1    0.000    0.000    0.000    0.000 __init__.py:7380(ValueStreamItem)
        1    0.000    0.000    0.000    0.000 exceptions.py:59(AWIPOperationError)
        1    0.000    0.000    0.000    0.000 greenlet.py:58(FailureSpawnedLink)
        1    0.000    0.000    0.000    0.000 io.py:84(BufferedIOBase)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:187(InterpolationDepthError)
        1    0.000    0.000    0.000    0.000 errors.py:63(DistutilsTemplateError)
        1    0.000    0.000    0.000    0.000 errors.py:59(DistutilsInternalError)
        1    0.000    0.000    0.000    0.000 io.py:81(RawIOBase)
        1    0.000    0.000    0.000    0.000 threading.py:749(_set_daemon)
        1    0.000    0.000    0.000    0.000 argparse.py:682(ArgumentError)
        1    0.000    0.000    0.000    0.000 argparse.py:837(_StoreConstAction)
        1    0.000    0.000    0.000    0.000 greenlet.py:381(_dummy_event)
        1    0.000    0.000    0.000    0.000 errors.py:76(CompileError)
        1    0.000    0.000    0.000    0.000 ascii.py:31(StreamReader)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:162(InterpolationError)
        1    0.000    0.000    0.000    0.000 ascii.py:24(IncrementalDecoder)
        1    0.000    0.000    0.000    0.000 errors.py:70(CCompilerError)
        1    0.000    0.000    0.000    0.000 errors.py:38(DistutilsOptionError)
        1    0.000    0.000    0.000    0.000 argparse.py:978(_HelpAction)
        1    0.000    0.000    0.000    0.000 pkg_resources.py:172(DistributionNotFound)
        1    0.000    0.000    0.000    0.000 event.py:30(is_set)
        1    0.000    0.000    0.000    0.000 errors.py:79(LibError)
        1    0.000    0.000    0.000    0.000 ConfigParser.py:183(InterpolationSyntaxError)
        1    0.000    0.000    0.000    0.000 argparse.py:1462(_ArgumentGroup)
        1    0.000    0.000    0.000    0.000 exceptions.py:47(AWIPClientDisconnected)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

