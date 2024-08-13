# Exploring-Azure-IoT
Connecting Virtual IoT devices to the Azure Cloud

---

# The Azure Command-Line Interface (CLI)

Verify you have successsfully installed the Azure CLI:
```
az --version
```
After you successfully install the Azure CLI, you must have at least v2.46.0 for the latest versions of azure-iot. <br/><br/>

Add the IoT specific extentions to your Azure CLI:
```
az extension add --name azure-iot
```
Update your Azure CLI IoT package:
```
az extension update --name azure-iot
```
Optional: To set Auto-Update (The CLI will regularly check for new versions and prompt the user to upgrade after each command)
```
az config set auto-upgrade.enable=yes
```



