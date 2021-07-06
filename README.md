# Important - Read these points first

- Original repo is <https://github.com/lzzy12/python-aria-mirror-bot>
- I have collected some cool features from various repositories and merged them in one.
- So, credits goes to original repo holder, not to me. I have just collected them.
- This (or any custom) repo is not supported in official bot support group.
- So if you have any issue then check first that issue is in official repo or not, You are only allowed to report that issue in bot support group if that issue is also present in official repo.

## **What is this repo about?**

This is a telegram bot writen in python for mirroring files on the internet to our beloved Google Drive.

## **Features supported**

## Additional Features

- Updater (**NOTE**: You must upload your **token.pickle** to Index and fill your **token.pickle** url to **TOKEN_PICKLE_URL**, because your **token.pickle** will deleted after update)
- Limiting size Torrent/Direct, Tar/Unzip, Mega, cloning Google Drive support
- Get detailed info about replied media (Only for Telegram file)
- Stop duplicate cloning Google Drive & mirroring Mega support
- Tar/Unzip Google Drive link support
- Speedtest with picture results
- Sudo with Database support
- Multiple Trackers support
- Check Heroku dynos stats
- Extracting **tar.xz** support
- Heroku config support
- Custom Image support
- Counting file/folder
- View Link button
- Shell and Eval
- Torrent search supported:

```comment
nyaasi, sukebei, 1337x, piratebay, tgx,
yts, eztv, torlock, rarbg
```

- Direct links supported:

```comment
letsupload.io, hxfile.co, anonfiles.com, fembed.com, femax20.com, layarkacaxxi.icu,
naniplay.com, naniplay.nanime.in, naniplay.nanime.biz, sbembed.com, streamsb.net,
feurl.com, pixeldrain.com, uptobox.com (Uptobox account must be premium),
1drv.ms (Only works for file not folder or business account)
```

## From Original Repos

- Mirroring direct download links, Torrent, and Telegram files to Google Drive
- Mirroring Mega.nz links to Google Drive (If your Mega account not premium, it will limit 5GB/6 hours)
- Copy files from someone's Drive to your Drive (Using Autorclone)
- Download/Upload progress, Speeds and ETAs
- Mirror all Youtube-dl supported links
- Docker support
- Uploading to Team Drive
- Index Link support
- Service Account support
- Delete files from Drive
- Shortener support
- Custom Filename (Only for URL, Telegram files and Youtube-dl. Not for Mega links and Magnet/Torrents)
- Extracting password protected files, using custom filename and download from password protected Index Links see these examples:

[![dev.to](https://img.shields.io/badge/see%20on%20telegraph-grey?style=for-the-badge)](https://telegra.ph/Magneto-Python-Aria---Custom-Filename-Examples-01-20)

- Extract these filetypes and uploads to Google Drive

```comment
ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2,
APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT,
HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS,
NTFS, RPM, SquashFS, UDF, VHD, XAR, Z.
```

## 👩‍🚒 **MODIFIED BY** : [**Juned KH**](https://t.me/kjuned007)

- [x] Cool and stylish Progress Bar
- [x] Change Requirment text
- [x] Now YTDL Fixed (with custom resolution and custom file name)
- [x] Fixing Minor bugs
- [x] Change Dockerfile

## 📭 **JOIN OUR MIRROR GROUP:** [JOIN HERE](https://t.me/torrent_to_drive)

## Bot commands to be set in botfather

```comment
mirror - Start Mirroring
tarmirror - Upload tar (zipped) file
unzipmirror - Extract files
clone - copy file/folder to drive
watch - mirror YT-DL support link
tarwatch - mirror youtube playlist link as tar
cancel - Cancel a task
cancelall - Cancel all tasks
del - Delete file from Drive
list - [query] searches files in G-Drive
status - Get Mirror Status message
stats - Bot Usage Stats
help - Get Detailed Help
speedtest - Check Speed of the host
log - Bot Log [owner only]
```

## **Generate Database**

<details>
    <summary>
        <b>Click here for more details</b></summary>

### **1. Using ElephantSQL**

- Go to <https://elephantsql.com/> and create account (skip this if you already have ElephantSQL account)
- Hit **Create New Instance**
- Follow the further instructions in the screen
- Hit **Select Region**
- Hit **Review**
- Hit **Create instance**
- Select your database name
- Copy your database url, and fill to **DATABASE_URL** in config

### **2. Using Heroku PostgreSQL**

[![dev.to](https://img.shields.io/badge/see%20on%20dev.to-black?style=for-the-badge&logo=dev-dot-to)](https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1)

**NOTE**: If you are deploying on Heroku using Heroku button, no need to generate database manually, because it will automatic generate database when first deploying

</details>

## **HOW TO DEPLOY** ?

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/junedkh/Torrent-Mirror/tree/master)

## **Deploying With Heroku Cli**

<details>
<summary><b>Click here for more details</b></summary>

- Run the script to generate token file(token.pickle) for Google Drive:

```bash
python3 generate_drive_token.py
```

- Install [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- Login into your heroku account with command:

```bash
heroku login
```

- Create a new heroku app:

```bash
heroku create appname
```

- Select This App in your Heroku-cli:

```bash
heroku git:remote -a appname
```

- Change Dyno Stack to a Docker Container:

```bash
heroku stack:set container
```

- Add Heroku Postgres (only if you are deploying it for the 1st time)

```bash
heroku addons:create heroku-postgresql
```

- Add Private Credentials and Config Stuff:

```bash
git add -f credentials.json token.pickle config.env heroku.yml
```

- Commit new changes:

```bash
git commit -m "Added Creds."
```

- Push Code to Heroku:

```bash
git push heroku master --force
```

- Restart Worker by these commands:

```bash
heroku ps:scale worker=0
```

```bash
heroku ps:scale worker=1
```

</details>

## **Setting up config file**

<details>
    <summary><b>Click Here For More Details</b></summary>

```bash
cp config_sample.env config.env
```

- Remove the first line saying:

```comment
_____REMOVE_THIS_LINE_____=True
```

Fill up rest of the fields. Meaning of each fields are discussed below:

### **Required Field**

- **BOT_TOKEN**: The Telegram bot token that you get from [@BotFather](https://t.me/BotFather)
- **TELEGRAM_API**: This is to authenticate to your Telegram account for downloading Telegram files. You can get this from <https://my.telegram.org> DO NOT put this in quotes.
- **TELEGRAM_HASH**: This is to authenticate to your Telegram account for downloading Telegram files. You can get this from <https://my.telegram.org>
- **OWNER_ID**: The Telegram user ID (not username) of the Owner of the bot
- **DATABASE_URL**: Your Database URL. See [Generate Database](https://github.com/junedkh/Torrent-Mirror/tree/master#generate-database) to generate database. (**NOTE**: If you deploying on Heroku using Heroku button, no need to generate database manually, because it will automatic generate database when first deploying)
- **GDRIVE_FOLDER_ID**: This is the folder ID of the Google Drive Folder to which you want to upload all the mirrors.
- **DOWNLOAD_DIR**: The path to the local folder where the downloads should be downloaded to
- **DOWNLOAD_STATUS_UPDATE_INTERVAL**: A short interval of time in seconds after which the Mirror progress message is updated. (I recommend to keep it `5` seconds at least)
- **AUTO_DELETE_MESSAGE_DURATION**: Interval of time (in seconds), after which the bot deletes it's message (and command message) which is expected to be viewed instantly. (**Note**: Set to `-1` to never automatically delete messages)
- **UPSTREAM_REPO**: Link for Bot Upstream Repo, if you want default update, fill `https://github.com/junedkh/Torrent-Mirror` .
- **UPSTREAM_BRANCH**: Branch name for Bot Upstream Repo, fill `master`.

### Optional Field

- **ACCOUNTS_ZIP_URL**: Only if you want to load your Service Account externally from an Index Link. Archive your Service Account json files to a zip file directly (don't archive the accounts folder. Select all the jsons inside and zip them only instead. Name the zip file with whatever you want, it doesn't matter). Fill this with the direct link of that file.
- **TOKEN_PICKLE_URL**: Only if you want to load your **token.pickle** externally from an Index Link. Fill this with the direct link of that file.
- **AUTHORIZED_CHATS**: Fill user_id and chat_id of you want to authorize.
- **IS_TEAM_DRIVE**: Set to `True` if `GDRIVE_FOLDER_ID` is from a Team Drive else `False` or Leave it empty.
- **USE_SERVICE_ACCOUNTS**: (Leave empty if unsure) Whether to use Service Accounts or not. For this to work see [Using Service Accounts](https://github.com/junedkh/Torrent-Mirror/tree/master#step-1-generate-service-accounts-what-is-service-account) section below.
- **INDEX_URL**: Refer to <https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index> The URL should not have any trailing '/'
- **MEGA_API_KEY**: Mega.nz api key to mirror mega.nz links. Get it from [Mega SDK Page](https://mega.nz/sdk)
- **MEGA_EMAIL_ID**: Your email id you used to sign up on mega.nz for using premium accounts (Leave th)
- **MEGA_PASSWORD**: Your password for your mega.nz account
- **BLOCK_MEGA_FOLDER**: If you want to remove mega.nz folder support, set it to `True`.
- **BLOCK_MEGA_LINKS**: If you want to remove mega.nz mirror support, set it to `True`.
- **STOP_DUPLICATE_MIRROR**: (Leave empty if unsure) if this field is set to `True`, bot will check file in Drive, if it is present in Drive, downloading will be stopped. (**Note**: File will be checked using filename, not using filehash, so this feature is not perfect yet)
- **STOP_DUPLICATE_MEGA**: (Leave empty if unsure) if this field is set to `True`, bot will check file in Drive, if it is present in Drive, downloading Mega will be stopped.
- **STOP_DUPLICATE_CLONE**: (Leave empty if unsure) if this field is set to `True`, bot will check file in Drive, if it is present in Drive, cloning will be stopped.
- **CLONE_LIMIT**: To limit cloning Google Drive (leave space between number and unit, Available units is (gb or GB, tb or TB).
- **MEGA_LIMIT**: To limit downloading Mega (leave space between number and unit, Available units is (gb or GB, tb or TB).
- **TORRENT_DIRECT_LIMIT**: To limit the Torrent/Direct mirror size, Leave space between number and unit. Available units is (gb or GB, tb or TB).
- **TAR_UNZIP_LIMIT**: To limit mirroring as Tar or unzipmirror. Available units is (gb or GB, tb or TB).
- **IMAGE_URL**: Show Image/Logo in /start message. Fill value of image your link image, use telegra.ph or any direct link image.
- **VIEW_LINK**: View Link button to open file Index Link in browser instead of direct download link, you can figure out if it's compatible with your Index code or not, open any video from you Index and check if the END of link from browser link bar is `?a=view`, if yes make it `True` it will work (Compatible with [Bhadoo Index](https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index) Code)
- **UPTOBOX_TOKEN**: Uptobox token to mirror uptobox links. Get it from [Uptobox Premium Account](https://uptobox.com/my_account).
- **HEROKU_API_KEY**: (Only if you deploying on Heroku) Your Heroku API key, get it from <https://dashboard.heroku.com/account>.
- **HEROKU_APP_NAME**: (Only if you deploying on Heroku) Your Heroku app name.
- **IGNORE_PENDING_REQUESTS**: (Optional field) If you want the bot to ignore pending requests after it restarts, set this to `True`.
- **SHORTENER_API**: Fill your Shortener api key if you are using Shortener.
- **SHORTENER**: if you want to use Shortener in Gdrive and index link, fill Shortener url here. Examples:

```comment
exe.io, gplinks.in, shrinkme.io, urlshortx.com, shortzon.com, linkvertise.com, shorte.st
```

Above are the supported url Shorteners. Except these only some url Shorteners are supported.

**Note**: You can limit maximum concurrent downloads by changing the value of **MAX_CONCURRENT_DOWNLOADS** in aria.sh. By default, it's set to `7`.

### Add more buttons (Optional Field)

Three buttons are already added of Drive Link, Index Link, and View Link, you can add extra buttons, these are optional, if you don't know what are below entries, simply leave them, don't fill anything in them.

- **BUTTON_FOUR_NAME**:
- **BUTTON_FOUR_URL**:
- **BUTTON_FIVE_NAME**:
- **BUTTON_FIVE_URL**:
- **BUTTON_SIX_NAME**:
- **BUTTON_SIX_URL**:

</details>

## Getting Google OAuth API credential file

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of mirror-bot, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate token file (token.pickle) for Google Drive:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```

## **Using service accounts for uploading to avoid user rate limit**

For Service Account to work, you must set USE_SERVICE_ACCOUNTS="True" in config file or environment variables
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) for the scripts

## **Generating service accounts**

## **Step 1. Generate service accounts [What is service account](https://cloud.google.com/iam/docs/service-accounts)**

Let us create only the service accounts that we need.
**Warning:** abuse of this feature is not the aim of autorclone and we do **NOT** recommend that you make a lot of projects, just one project and 100 sa allow you plenty of use, its also possible that overabuse might get your projects banned by google.

```comment
Note: 1 service account can copy around 750gb a day, 1 project makes 100 service accounts so thats 75tb a day, for most users this should easily suffice.
```

``` bash
python3 gen_sa_accounts.py --quick-setup 1 --new-only
```

A folder named accounts will be created which will contain keys for the service accounts created

NOTE: If you have created SAs in past from this script, you can also just re download the keys by running:

```bash
python3 gen_sa_accounts.py --download-keys project_id
```

### Add all the service accounts to the Team Drive or folder

- Run:

```bash
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```

## **Youtube-dl authentication using .netrc file**

For using your premium accounts in youtube-dl, edit the netrc file (in the root directory of this repository) according to following format:

```sh
machine host login username password my_youtube_password
```

where host is the name of extractor (eg. youtube, twitch). Multiple accounts of different hosts can be added each separated by a new line

## **Credits**

Thanks to:

- [out386](https://github.com/out386) heavily inspired from Telegram Bot which is written in JS
- [Izzy12](https://github.com/lzzy12/) for original repo
- [Dank-del](https://github.com/Dank-del/) for base repo
- [magneto261290](https://github.com/magneto261290/) for some features
- [SVR666](https://github.com/SVR666/) for some features & fixes
- [anasty17](https://github.com/anasty17) for some features & help
- [breakdowns](https://github.com/breakdowns) for slam-mirrorbot

And many more people who aren't mentioned here, but may be found in [Contributors](https://github.com/junedkh/Torrent-Mirror/graphs/contributors).
