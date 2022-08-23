import requests
import sys

def YT(link):
    
    def Download_And_Save(name , url):
        a = requests.get(url)
        try:
            with open(name , "wb") as file:
                for chunk in a.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            return True
        except:
            return False

    def GET_AUDIO_DETAILS(link):
        url = "https://yt5s.com/api/ajaxSearch"
        data = {
            "q":link,
            "vt":"mp3"
        }
        res = requests.post(url=url , data=data)
        vid = res.json()['vid']
        title = res.json()['title']
        token = res.json()['token']
        timeExpires = res.json()['timeExpires']
        return (vid , title , token , timeExpires)

    def GET_AUDIO_URL(link):
        url = "https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994"
        vid , title , token , timeExpires = GET_AUDIO_DETAILS(link)
        data = {"v_id":vid,
            "ftype":"mp3",
            "fquality":"128",
            'token':token,
            "timeExpire":timeExpires,
            "client":"yt5s.com"}
        
        header = {"X-Requested-Key":"de0cfuirtgf67a"}
        
        res = requests.post(url=url ,headers=header, data=data)
        video_url = res.json()['d_url']
        video_name = str(title).split("|")[0] +".mp3"
        if Download_And_Save(video_name , video_url) == True:
            
            print("[+] Video Download compleate..:)")
        else:
            print("[+] Video Download Failed..!")

    GET_AUDIO_URL(link)
    
    
    
if __name__ == "__main__":    
    cmd = sys.argv
    if len(cmd) >1:
        links = cmd[1:]
        for i in links:
            YT(i)
    else:
        print("\n[+] Command Example : python3 Downloader.py 'link' 'link'\n")
        link = input("Enter YT LINK : ")
        YT(link)
