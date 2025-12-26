# pickle load example
# WARNING: pickle.load() can execute arbitrary code and should only be used
# with trusted data. For untrusted data, use safer alternatives like JSON.
# See: https://docs.python.org/3/library/pickle.html#module-pickle
import pickle
import random
import os

# Only load pickle files from trusted sources in trusted locations
pickle_file = 'assets/discordia.pkl'

# Verify the file exists and is in the expected location
if not os.path.exists(pickle_file):
    raise FileNotFoundError(f"Pickle file not found: {pickle_file}")

# Resolve to absolute path to prevent path traversal
pickle_file = os.path.abspath(pickle_file)
expected_dir = os.path.abspath('assets')

if not pickle_file.startswith(expected_dir):
    raise ValueError("Pickle file must be in the assets directory")

with open(pickle_file, 'rb') as f:
    # SECURITY NOTE: This loads a pickle file that must be from a trusted source
    # Never load pickle files from untrusted sources (user uploads, internet, etc.)
    discordia = pickle.load(f)


def getran(tex):
    texter = random.choice(tex)
    if len(texter) < 140 and len(texter) > 0:
        return texter
    else:
        globular = getran(tex)
    return globular


def to140(data):
    loser = []
    for listitem in data:
        if len(listitem) < 140 and len(listitem) > 0:
            loser.append(listitem)
    return loser


print(getran(discordia))
exit('there ya go')
