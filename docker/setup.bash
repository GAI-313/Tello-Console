# macos
#!bin/bash
pip=`pip3 -V`
docv=`docker -v`
brew=`brew --version`
cd ~

echo "HomeBrew の確認を行います…"
while [[ ! $brew =~ "Homebrew" ]]
do
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
done
echo "HomeBrew を確認しました…"
echo "pip の確認を行います…"
while [[ ! $pip =~ "$HOME" ]]
do
    sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
done
echo "pip を確認しました。OpenCV、Numpy をインストールします…"
pip3 install opencv-python
echo "Dokcer の確認を行います…"
while [[ ! $docv =~ "Docker version" ]]
do
    echo "Docker をインストールします…"
    brew install --cask docker
    open /Applications/Docker.app 
    docv=`docker -v`
done
echo "Docker を確認しました…"
echo "Ubuntu 20.04 イメージをダウンロードします…"

echo "done"