
## Get your Primary connection string from the Azure CLI
```

az iot hub device-identity connection-string show --hub-name <YOUR-IOT-HUB-NAME> --device-id <YOUR-IOT-DEVICE-NAME>
```

## Generate your SAS token from the Azure CLI
```

az iot hub generate-sas-token -n <YOUR-IOT-HUB-NAME> -d <YOUR-IOT-DEVICE-NAME> --du 999999
```
