@echo off
REM Script para ativar o ambiente virtual e executar o bot

echo ========================================
echo   Bot do Instagram - Ativando ambiente
echo ========================================
echo.

REM Ativar ambiente virtual
call .\venv\Scripts\activate.bat

echo [OK] Ambiente virtual ativado com Python 3.11!
echo.
echo Para executar o bot, use: python main.py
echo Para sair do ambiente: deactivate
echo.
call python main.py

REM Manter o terminal aberto
cmd /k
