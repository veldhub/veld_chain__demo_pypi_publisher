# ![veld chain](https://raw.githubusercontent.com/veldhub/.github/refs/heads/main/images/symbol_V_letter.png) veld_chain__demo_pypi_publisher

This repo contains a [chain veld](https://zenodo.org/records/13322913) encapsulating a demo publishing
workflow to pypi.org . 

The demo python module can be found at [./data/test_python_module/](./data/test_python_module/) .

## requirements

- git
- docker compose (note: older docker compose versions require running `docker-compose` instead of 
  `docker compose`)

Clone this repo with all its submodules
```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__demo_pypi_publisher.git
```

## how to reproduce

**[./veld_publish.yaml](./veld_publish.yaml)** 

Builds and publishes the demo python module. A password or token must be supplied. For more
information, see the veld yaml file.

Execute with:

```
docker compose -f veld_publish.yaml up
```
