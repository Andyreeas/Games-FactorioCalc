# Games-FactorioCalc

Factorio Calculator

# Backend

## DB .txt file
extract from Factorio with lua command:

/silent-command
game.player.force.enable_all_recipes()
game.player.force.enable_all_technologies()
game.player.force.research_all_technologies(1)

/silent-command
listresources = {}
for a, b in pairs(game.player.force.recipes) do
    item = b.name .. " @ " .. b.energy .. " seconds @ Produces : "
    for c,d in pairs (b.products) do
        if d.amount ~= nil then    
            item = item .. d.amount .. ":" .. d.name .. ", "
        end
    end
    item = item .. " @ Ingredients: "
    for x,y in pairs (b.ingredients) do
        item = item .. y.amount .. ":" .. y.name .. ", "
    end
    table.insert(listresources,item) 
end
table.sort(listresources)
game.write_file("recipies.txt", table.concat(listresources, "\r\n"))

## Results
C:\Users\YOUR_NAME\AppData\Roaming\Factorio\script-output\recipies.txt


# Frontend
evt. GUI or simple CLI

## Calculations
Time to craft an Item include efficiency/ speed/ productivity modules

Number of assemblers needed to fill the Belt (#Assembling time) or empty the source
