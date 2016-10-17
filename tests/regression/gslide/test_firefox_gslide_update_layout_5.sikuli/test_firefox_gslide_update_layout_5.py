# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.
sys.path.append(sys.argv[2])
import browser
import common
import gslide

com = common.General()
ff = browser.Firefox()
gs = gslide.gSlide()

ff.clickBar()
ff.enterLink(sys.argv[3])

sleep(2)
gs.wait_for_loaded()

gs.invoke_layout_list()
type(Key.DOWN)
sleep(0.5)
type(Key.DOWN)
sleep(0.5)
type(Key.ENTER)
waitVanish(gs.theme_mozilla_tag_red)
