from imagebase import *
import math
class clubdance():
    leftsign = (247,250)
    upsign =(348,242) 
    downsign =(432,289)
    rightsign = (531,250)
    sign_empty_color = (166,166,166)
    validgame = (967,139)
    validgamecolor = (254,254,254)
    # Can add features over here for use



    
def scangame(image = None):
    '''
    scangame() returns str: 4 with 0 or 1 depending on wether there is an arrow or not.
    '''
    if image == None:
        image = ImageGrab.grab()
    string = ["0","0","0","0"]
    '''
    if image.getpixel(clubdance.leftsign) != clubdance.sign_empty_color:
        string[0] = "1"
    if image.getpixel(clubdance.upsign) != clubdance.sign_empty_color:
        string[1] = "1"
    if image.getpixel(clubdance.rightsign) != clubdance.sign_empty_color:
        string[2] = "1"
    if image.getpixel(clubdance.downsign) != clubdance.sign_empty_color:
        string[3] = "1"
    '''
    if isleft(image.getpixel(clubdance.leftsign) ):
        string[0] = "1"
    if isup(image.getpixel(clubdance.upsign)   ):
        string[1] = "1"
    if isright(image.getpixel(clubdance.rightsign)):
        string[2] = "1"
    if isdown(image.getpixel(clubdance.downsign) ):
        string[3] = "1"
    return ''.join(string)

def loop():
    #Check for valid game :)
    myimage = ImageGrab.grab()

def issmoke(nums):
    # smoke is 230,204,230
    # give 10 dist to smoke
    return math.sqrt( abs(nums[0]-230)**2 + abs(nums[1]-204)**2 + abs(nums[2]-230)**2) <= 10
def isup(nums):
    return math.sqrt( abs(nums[0]-255)**2 + abs(nums[1]-226)**2 + abs(nums[2]-5)**2) <= 10
def isleft(nums):
    return math.sqrt( abs(nums[0]-213)**2 + abs(nums[1]-108)**2 + abs(nums[2]-24)**2) <= 10
def isright(nums):
    return math.sqrt( abs(nums[0]-84)**2 + abs(nums[1]-124)**2 + abs(nums[2]-223)**2) <= 10 or math.sqrt( abs(nums[0])**2 + abs(nums[1]-61)**2 + abs(nums[2]-208)**2) <= 10
def isdown(nums):
    return math.sqrt( abs(nums[0]-213)**2 + abs(nums[1]-108)**2 + abs(nums[2]-24)**2) <= 10

def illustratelog(lst):
	idx = 0
	incidentnumber = 1
	lastincedent = -2
	while idx  < len(lst):
		if lst[idx] != "OK":
			if lastincedent + 1 != idx:
				print "Incident %s"%(incidentnumber)
				incidentnumber += 1
				lastincedent = idx
				print lst[idx]
			else:
				print lst[idx]
				lastincedent += 1
		idx += 1



		
start = False
log = [[],[],[],[]]
while True:
    im = ImageGrab.grab()
    c = scangame()
    tosay = []
    pl = [clubdance.leftsign,clubdance.upsign,clubdance.rightsign,clubdance.downsign]
    idx = 0
    for i in c:
        if i== "0":
            if not start:
                print "Data collection started!"
                start = True
            if start:
                log[idx].append("OK")
            tosay.append("OK")
        elif i == 1:
            if start:
                log[idx].append(         str(im.getpixel(pl[idx]))        )
        else:
            log.append("UF")
            tosay.append("UF")
        idx += 1
