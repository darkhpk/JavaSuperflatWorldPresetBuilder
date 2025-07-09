#!/usr/bin/env python3

LayerHeights: list[int] = [1, 2, 1]
Layers: list[str] = ["bedrock", "dirt", "grass"]

Biome: str = "plains"

BlockID: dict[str] = {
    "bedrock" : "bedrock",
    "dirt" : "dirt",
    "grass" : "grass_block",
}

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

def ListLayers():
    global Layers, LayerHeights, Biome
    print(" Biome type: "+Biome.capitalize()+"\n")
    print("  Layer | Height | Block")
    print("  ==================================")
    for element in range(len(LayerHeights)):
        reverse_block_index: int = len(LayerHeights) - element - 1
        block_height_str = str(LayerHeights[reverse_block_index])
        block_height_str = (" " * (6 - len(block_height_str))) + block_height_str
        print((" " * (7 - len(str(element)))) + str(element), end=" | ")
        print(block_height_str, end=" | ")
        print(Layers[reverse_block_index].capitalize())

def AddLayer():
    global Layers, LayerHeights
    ListLayers()

ListLayers()