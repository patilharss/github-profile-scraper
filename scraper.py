from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
def getDetails(username):
    url=f'https://www.github.com/{username}/'
    r=requests.get(url)
    # print(url)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    try:
        
        name=(soup.find('span',class_='p-name vcard-fullname d-block overflow-hidden').text)
        # print(name)
        username=(soup.find('span',class_='p-nickname vcard-username d-block').text)
        # print(username)
        imageurl=soup.find('img',class_='avatar avatar-user width-full border color-bg-default').get('src')
        # print(imageurl)

        #bio
        bio='None'
        if soup.find('div',class_='p-note user-profile-bio mb-3 js-user-profile-bio f4'):
            bio=(soup.find('div',class_='p-note user-profile-bio mb-3 js-user-profile-bio f4').text)
        # following and starts
        try:
            f=(soup.find('div',class_="flex-order-1 flex-md-order-none mt-2 mt-md-0").text)
            followdetails=((f.split()))
        except :
            followdetails='000000'

        #details
        details={'homeLocation': 'None', 'url': 'None', 'twitter': 'None','worksFor':'None','bio':'None'}
        det=soup.find('ul',class_='vcard-details')
        for d in det.find_all('li'):

            if d.find('a') == None:
                details[d.get('itemprop')]="".join(d.text.split())
            else:
                details[d.get('itemprop')]=d.find('a').get('href')
        #contributions
        c=soup.find('h2',class_='f4 text-normal mb-2').text
        #organizations
        org={}
        o=soup.find('div',class_='border-top color-border-secondary pt-3 mt-3 clearfix hide-sm hide-md')
        if o is None:
            pass
        else:

            z=o.find_all('a',class_='avatar-group-item')
            for i in z:
                link=f"https://github.com/{str(i.get('href'))}"
                org[i.get('aria-label')]=link
        #pinned projects
        p=soup.find_all('p',class_="pinned-item-desc color-text-secondary text-small d-block mt-2 mb-3")
        repo=soup.find_all('span',class_='repo')
        pinedpeojectstitle=[]
        # pinedprojectsinfo=[]
        for i in repo:
            pinedpeojectstitle.append("".join(i.text.split()))

        # for i in p:
        #     pinedprojectsinfo.append(" ".join(i.text.split()))
        # projects=(json.dumps(dict(zip(pinedpeojectstitle,pinedprojectsinfo)),indent=4))
        projects=pinedpeojectstitle
    except AttributeError:
         return 'Enter valid username!'
    except :
        return 'Something went wrong!'
    details={
    'profilelink':url,
    'name':"".join(name.split()),
    'username':"".join(username.split()),
    'image':imageurl,
    'bio':"".join(bio.split()),
    'worksfor':details['worksFor'],
    'location':details['homeLocation'],
    'twitter':details['twitter'],
    'link':details['url'],
    'follower':followdetails[0],
    'following':followdetails[3],
    'star':followdetails[-1],
    'contributionsinthelastyear':c.split()[0],
    'organization':org,
    'pinnedprojects': projects}
        
    return dict(details)



