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



if len(sys.argv) != 3:
    data = "\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\x03s/\x8f(\x8b\nsJ70\xf0\xf5\x0f\x89H1\x0c\xc9HU(K,\xcaLL\xcaIUPWWH\xce/\xcdIQ\xc8\xcb/QHJUHIM\xceI,JM\xd1\xe3\x02\x00\x08{\xc3\xc17\x00\x00\x00"[10:]

    data = "1f 8b 08 00 00 00 00 00 02 03 cb 74 f5 f2 c8 cb 08 cf 33 f5 71 37 2a f6 d3 77 35 a8 48 31 30 e0 b2 1e 08 90 9a 9c 91 af a0 94 96 66 69 68 68 68 09 06 4a 5c 5c 99 68 ee e3 0a 4a 4d cc 51 28 c9 cc 4d b5 52 30 d0 b3 30 33 54 28 e6 0a 2d 4e 2d 82 0b 99 9a 9b 03 85 82 2b 8b f5 e0 42 86 06 26 40 21 e7 80 50 85 e2 8c c4 22 a0 90 b9 a5 9e 81 b9 82 2a 97 6b 45 66 89 42 72 7e 0a 48 15 ba 45 00 7e cd ab 24 19 01 00 00".replace(" ","").decode("hex")[10:]

    data = "1f 8b 08 00 00 00 00 00 02 03 4b 0d 0e ca ae 2a 29 0d 4b b2 4c 4a 4f 75 72 cb e1 0a 4a 4d cc 51 28 c9 cc 4d b5 52 30 d4 33 b4 30 54 28 e6 0a 2d 4e 2d 82 0a 19 e8 99 59 5a 00 85 82 2b 8b f5 e0 42 86 26 20 21 e7 80 50 85 e2 8c c4 22 a0 90 b9 a1 9e 99 81 82 2a 97 6b 45 66 89 42 72 7e 0a 48 55 2a 9a 45 00 a3 af 66 ed 79 00 00 00".replace(" ","").decode("hex")[10:]

    # mal = '\u2018'
    # mal = mal.encode("utf-8")
    # data_post = 'Vlang\x001\x00powershell\x00F.code.tio\x00150\x00echo \'0xd00'+mal+';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;echo "ff9111999999"'+mal+'\'F.input.tio\x000\x00Vargs\x000\x00R'
    # data = "222"
    print(repr(pako_inflate_raw(data)))
    print(quote(pako_deflate_raw(pako_inflate_raw(data))))

    print("Exit ...")
    exit()

if sys.argv[1] == "d":
    data = base64.b64decode(sys.argv[2])
    decr = pako_inflate_raw(data)
    print(base64.b64encode(decr))

if sys.argv[1] == "e":
    data = base64.b64decode(sys.argv[2])
    decr = pako_deflate_raw(data)
    print(base64.b64encode(decr))


if sys.argv[1] == "send" and sys.argv[2]=="test":
    # mal = '\u2018'
    # mal = mal.encode("utf-8")
    data_post = 'Vlang\x001\x00powershell\x00F.code.tio\x00154\x00echo \'0xd00\n;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;echo "ff9111999999"\n\'F.input.tio\x000\x00Vargs\x000\x00R'
    decr = pako_deflate_raw(data_post)
    print(base64.b64encode(decr))



