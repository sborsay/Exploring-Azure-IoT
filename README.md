# Exploring-Azure-IoT
Connecting Virtual IoT devices to the Azure Cloud

---

# The Azure Command-Line Interface (CLI)

Add: az extension add --name azure-iot<p>
Update: az extension update --name azure-iot


The Azure Command-Line Interface (CLI) has an in-tool command that can automatically update the CLI and all installed extensions:
Run the command az config set auto-upgrade.enable=yes
The CLI will regularly check for new versions and prompt the user to upgrade after each command finishes running 




Install the Azure CLI. You must have at least v2.46.0 for the latest versions of azure-iot , which you can verify with az --version.
Add, Update or Remove the IoT extension with the following commands: Add: az extension add --name azure-iot. Update: az extension update --name azure-iot


