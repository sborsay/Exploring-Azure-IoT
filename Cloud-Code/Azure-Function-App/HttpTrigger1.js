const { CosmosClient } = require("@azure/cosmos");
module.exports = async function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
        const endpoint = "<Your-CosmosDB-Endpoint-Here>"; //Example: "https://myCosmosDB123.documents.azure.com:443";
        const key =
            "<Your-CosmosDB-Primary-Key-Here>";  
        const databaseId = "ToDoList";
        const containerId = "Items";
    context.log(' Going to retrive....');
    try{
         const client = new CosmosClient({ endpoint, key });
        const database = client.database(databaseId);
        const container = database.container(containerId);
            const { resources } = await container.items.readAll().fetchAll();
        //const resources = await container.item("1", "1").read();
        console.log("result" + JSON.stringify(resources));

        return context.res = {
            status: 200,
            body: JSON.stringify(resources),
        };
    }catch(error){
        context.log("Error"+error);
    }
}
