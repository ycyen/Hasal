
sys.path.append(sys.argv[2])
import browser
import common

com = common.General()
ff = browser.Firefox()

ff.clickBar()
ff.enterLink(sys.argv[3])

sleep(2)
wait(Pattern('twitter_com.png').similar(0.80), 60)