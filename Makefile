install:
	ln -s `readlink -e powerline-shell.py` ~/powerline-shell.py
	mkdir -p ~/.fonts/
	cp ./fonts/PowerlineSymbols.otf ~/.fonts/
	fc-cache -vf ~/.fonts/
	mkdir -p ~/.config/fontconfig/conf.d/
	cp ./fonts/10-powerline-symbols.conf ~/.config/fontconfig/conf.d/

	python ./install.py

	cat << EOF >> ~/.bashrc
	function _update_ps1() {
     export PS1="$(~/powerline-shell.py $? 2> /dev/null)"
  }
  export PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
	EOF
