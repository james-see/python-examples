from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
instauser = "default"


def getuser():
    """Get instagram username."""
    instauser = input('What instagram user to get information about? ["q" for quit]: ')
    return instauser


def getcontent(instauser):
    """Headless chrome gets the content we need."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://www.instagram.com/{}/'.format(instauser))
    print(driver.title)
    userdata = driver.execute_script("return _sharedData.entry_data.ProfilePage[0].graphql.user")
    # print all of the data
    print(f"User ID: {userdata['id']}\n\
        Biography: {userdata['biography']}\n\
            Friends: {userdata['edge_followed_by']['count']}\n\
                Following: {userdata['edge_follow']['count']}")


def main():
    """Run the program."""
    instauser = getuser()
    if instauser != 'q':
        getcontent(instauser)
    else:
        print('Thanks for playing.')


if __name__ == "__main__":
    main()
