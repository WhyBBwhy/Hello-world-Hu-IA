#!/bin/bash

FILE_PATH="./system.log"
ERROR_CODE=1

if [ -f "$FILE_PATH"  ]; then
	echo "Лог-файл найден."
	ERROR_CODE=0
else
	echo "Ошибка: файл не существует"
fi

case $ERROR_CODE in
	0)
		echo "Статус: ошибок нет"  ;;
	1)
		echo "Статус: критическая ошибка!" ;;
	*)
		echo "Статус: неизвестный код"
esac
