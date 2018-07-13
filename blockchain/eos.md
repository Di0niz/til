# Установка и настройка блокчейн EOS

## Автоматическая настройка

Минимальные системные требования:

  ОЗУ: 8 Gb

В качестве основного дистрибутива выбрал CentOS 7 64.

### Предварительные настройки

Установка региональных настроек:

```sh
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_COLLATE=C
export LC_CTYPE=en_US.UTF-8
```

Установка дистибутива GIT:

```sh
sudo yum install git -y
```

Дополнительно можно изменить требования по оперативной памяти:

```sh
vi scripts/eosio_build_centos.sh 
```

### Установка

Скачивание дистрибутива:


```sh
git clone https://github.com/EOSIO/eos --recursive
```

Переход в директорию и начала сборки:

```sh
cd eos
./eosio_build.sh
```

### Настройка

Изменение файла конфигурации

```sh
vi ~/.local/share/eosio/nodeos/config/config.ini
```

Дополнительные плагины:

- eosio::chain_api_plugin
- eosio::history_api_plugin
- eosio::http_plugin
- eosio::wallet_api_plugin

### Запуск 

```sh
./nodeos -e -p eosio --plugin eosio::chain_api_plugin --plugin eosio::history_api_plugin --plugin eosio::http_plugin --plugin eosio::wallet_api_plugin
```

Для подключения к блокчейну рекомендует определить параметры подключения через alias:

```sh
alias cleos='/root/eos/build/programs/cleos/cleos --url http://localhost:8888 --wallet-url http://localhost:8888'
```

### Возможные проблемы

Если запущен keosd, то его лучше грохнуть:

```sh
pkill keosd 
```

Изменения конфигурационного файла, в основном связаны с утилитой keosd.
