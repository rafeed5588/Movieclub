if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/NEGANTG/cvilla-jan23.git /cvilla-jan23
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /cvilla-jan23
fi
cd /cvilla-jan23
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
