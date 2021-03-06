
#Copy this file to config.py, then amend the settings below according to
#your system configuration.

sdk_path = "/opt/android-sdk"
ndk_path = "/opt/android-ndk"

#You probably don't need to change this...
javacc_path = "/usr/share/java"

repo_url = "http://f-droid.org/repo"
repo_name = "FDroid"
repo_icon = "fdroid-icon.png"
repo_description = """
Replace this text by description of your repository
"""

#The key (from the keystore defined below) to be used for signing the
#repository itself. Can be None for an unsigned repository.
repo_keyalias = None

#The keystore to use for release keys when building. This needs to be
#somewhere safe and secure, and backed up!
keystore = "/home/me/somewhere/my.keystore"

#The password for the keystore (at least 6 characters).
keystorepass = "password1"

#The password for keys - the same is used for each auto-generated key
#as well as for the repository key.
keypass = "password2"

#The distinguished name used for all keys.
keydname = "CN=Birdman, OU=Cell, O=Alcatraz, L=Alcatraz, S=California, C=US"

#Use this to override the auto-generated key aliases with specific ones
#for particular applications. Normally, just leave it empty.
keyaliases = {}
keyaliases['com.example.app'] = 'example'

#The ssh path to the server's public web root directory. This is used for
#uploading data, etc.
serverwebroot = 'user@example:/var/www/repo'

