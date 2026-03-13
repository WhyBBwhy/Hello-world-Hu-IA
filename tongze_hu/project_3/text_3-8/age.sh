#!/bin/bash

CURRENT_YEAR=2026

read -p "Введите год своего рождения: " BIRTH_YEAR

AGE=$((CURRENT_YEAR - BIRTH_YEAR))

echo "Вам примерно: $AGE"
