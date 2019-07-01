from selenium import webdriver

# lets ask the user for an instagram user to look up
# globals
instauser = "default"

# functions


def getuser():
    """Get instagram username."""
    instauser = input('What instagram user to get information about? ["q" for quit]: ')
    return instauser


def getcontent(instauser):
    """Headless chrome gets the content we need."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.instagram.com/{}/'.format(instauser))
    print(driver.title)
    userdata = driver.execute_script("return _sharedData.entry_data.ProfilePage[0].graphql.user")
    # print all of the data
    print(f"User ID: {userdata['id']}\nBiography: {userdata['biography']}\nFriends: {userdata['edge_followed_by']['count']}\nFollowing: {userdata['edge_follow']['count']}")


def main():
    """Run the program."""
    global instauser
    while instauser != 'q':
        instauser = getuser()
        if instauser != 'q':
            getcontent(instauser)
        else:
            print('Thanks for playing.')
            raise SystemExit(0)

if __name__ == "__main__":
    main()
    raise SystemExit(0)
