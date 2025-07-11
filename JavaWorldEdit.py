#!/usr/bin/env python3

LayerHeights: list[int] = [1, 2, 1]
Layers: list[str] = ["bedrock", "dirt", "grass_block"]

Biome: str = "plains"

BlockID: list[str] = [
    "air",
    "bedrock",
    "obsidian",
    "crying_obsidian",
    "stone",
    "infested_stone",
    "diamond_ore",
    "iron_ore",
    "gold_ore",
    "copper_ore",
    "coal_ore",
    "emerald_ore",
    "redstone_ore",
    "lapis_ore",
    "raw_iron_block",
    "raw_copper_block",
    "raw_gold_block",
    "deepslate",
    "infested_deepslate",
    "deepslate_diamond_ore",
    "deepslate_iron_ore",
    "deepslate_gold_ore",
    "deepslate_copper_ore",
    "deepslate_coal_ore",
    "deepslate_emerald_ore",
    "deepslate_redstone_ore",
    "deepslate_lapis_ore",
    "coal_block",
    "amethyst_block",
    "diamond_block",
    "iron_block",
    "gold_block",
    "copper_block",
    "coal_block",
    "emerald_block",
    "redstone_block",
    "lapis_block",
    "tuff",
    "calcite",
    "andesite",
    "diorite",
    "granite",
    "basalt",
    "blackstone",
    "ice",
    "packed_ice",
    "blue_ice",
    "moss_block",
    "gravel",
    "clay",
    "sand",
    "sandstone",
    "red_sand",
    "red_sandstone",
    "dripstone_block",
    "prismarine",
    "magma_block",
    "lava",
    "water",
    "dirt",
    "ancient_debris",
    "grass_block",
]

BiomeID: dict[str] = {
    "plains" : "plains",
}

def GetBlockID(block: str = "dirt"):
    return "minecraft:"+block

def GetBiomeID(biome: str = "plains"):
    return "minecraft:"+BiomeID[biome]

def GetPresetName():
    global Layers, LayerHeights, Biome
    preset_name: str = ""
    if len(Layers) != len(LayerHeights):
        print("Number of layer heights not equal to layer names!")
        return ""
    for element in range(len(LayerHeights)):
        if LayerHeights[element] == 0:
            print("Layer heights can not be zero!")
            return ""
        if LayerHeights[element] == 1:
            preset_name += GetBlockID(Layers[element])
        else:
            preset_name += str(LayerHeights[element])+"*"+GetBlockID(Layers[element])
        if element != len(LayerHeights) - 1:
            preset_name += ","
        else:
            preset_name += ";"
    preset_name += GetBiomeID(Biome)
    return preset_name

def ListPresetName():
    print(GetPresetName())

def SavePresetName():
    file_name = input("Please enter a filename for the save file: ")
    try:
        file_fd = open(file_name, "w")
        file_fd.write(GetPresetName())
        file_fd.close()
        print("Saved successfully!")
    except FileNotFoundError:
        print("Could not create file '"+file_name+"'")

def Cleanup():
    global Layers, LayerHeights, Biome
    layer_removals_deferred: list[int] = []
    for layer in range(len(Layers)):
        if layer > 0:
            if Layers[layer] == Layers[layer - 1]:
                LayerHeights[layer] += LayerHeights[layer - 1]
                layer_removals_deferred += [layer - 1]
    for item in layer_removals_deferred:
        Layers.pop(item)
        LayerHeights.pop(item)

def ListLayers():
    global Layers, LayerHeights, Biome
    Cleanup()
    print(" Biome type: "+Biome.capitalize()+"\n")
    print("  Layer | Height | Block")
    print("  ======================")
    for element in range(len(LayerHeights)):
        reverse_block_index: int = len(LayerHeights) - element - 1
        block_height_str = str(LayerHeights[reverse_block_index])
        block_height_str = (" " * (6 - len(block_height_str))) + block_height_str
        print((" " * (7 - len(str(element)))) + str(element), end=" | ")
        print(block_height_str, end=" | ")
        print(Layers[reverse_block_index].capitalize())
    print("Total height: "+str(GetLayersHeight()))

def GetLayersHeight():
    total_height: int = 0
    for height in LayerHeights:
        total_height += height
    return total_height

def TestLayersHeight():
    total_height: int = GetLayersHeight()
    if total_height > 320:
        return 1
    elif total_height > 256:
        return 2
    else:
        return 0

def RemoveLayer():
    global Layers, LayerHeights
    ListLayers()
    layer_number: int = int(input("\nPlease select a layer to remove: "))
    if layer_number < 0:
        print("Layer number cannot be less than 0")
        return
    elif layer_number > len(Layers) - 1:
        print("Layer number cannot be higher than the number of layers")
        return
    reverse_layer_index: int = len(LayerHeights) - layer_number - 1
    Layers.pop(reverse_layer_index)
    LayerHeights.pop(reverse_layer_index)
    ListLayers()

def AddLayer():
    global Layers, LayerHeights
    ListLayers()
    layer_number: int = int(input("\nPlease select an index to insert this layer into: "))
    if layer_number < 0:
        print("Layer number cannot be less than 0")
        return
    elif layer_number > len(Layers):
        print("Layer number cannot be higher than the number of layers + 1")
        return
    block_name: str = input("Please choose a block for this layer: ").lower()
    if block_name not in BlockID:
        print("Invalid block name '"+block_name+"'")
        return
    else:
        block_height: int = int(input("Please select a height for this layer: "))
        reverse_layer_index: int = len(LayerHeights) - layer_number
        print(reverse_layer_index)
        Layers.insert(reverse_layer_index, block_name)
        LayerHeights.insert(reverse_layer_index, block_height)
        print("New layer configuration: ")
        ListLayers()

def main():
    print("Java world preset editor")
    print("Type a command or 'help' for a list of commands, or 'exit' to leave")
    while True:
        command = input(" > ")
        if command == "help":
            print(" list   - list all layers")
            print(" add    - add a layer")
            print(" remove - remove a layer")
            print(" get    - prints out the preset string")
            print(" save   - saves the preset string to a file")
        elif command == "list":
            try:
                ListLayers()
            except:
                print("Some error occurred when listing current layers")
        elif command == "add":
            try:
                AddLayer()
            except:
                print("Some error occurred when adding a layer")
        elif command == "remove":
            try:
                RemoveLayer()
            except:
                print("Some error occurred when removing a layer")
        elif command == "get":
            try:
                ListPresetName()
            except:
                print("Some error occurred when listing a preset")
        elif command == "save":
            try:
                SavePresetName()
            except:
                print("Some error occurred when saving a preset")
        elif command == "exit":
            return
        else:
            print("Command '"+command+"' is not recognised, please try again")

if __name__ == "__main__":
    main()