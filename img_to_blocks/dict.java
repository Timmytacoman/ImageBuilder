package me.timmytacoman.buildImage;

import java.util.*;

import org.bukkit.Material;

public class dict {
	public static Material get_value(String s) {
		// Initializing a Dictionary
		Dictionary edu = new Hashtable();
		// put() method
		edu.put("WHITE_CONCRETE", Material.WHITE_CONCRETE);
		edu.put("ORANGE_CONCRETE", Material.ORANGE_CONCRETE);
		edu.put("MAGENTA_CONCRETE", Material.MAGENTA_CONCRETE);
		edu.put("LIGHT_BLUE_CONCRETE", Material.LIGHT_BLUE_CONCRETE);
		edu.put("YELLOW_CONCRETE", Material.YELLOW_CONCRETE);
		edu.put("LIME_CONCRETE", Material.LIME_CONCRETE);
		edu.put("PINK_CONCRETE", Material.PINK_CONCRETE);
		edu.put("GRAY_CONCRETE", Material.GRAY_CONCRETE);
		edu.put("LIGHT_GRAY_CONCRETE", Material.LIGHT_GRAY_CONCRETE);
		edu.put("CYAN_CONCRETE", Material.CYAN_CONCRETE);
		edu.put("PURPLE_CONCRETE", Material.PURPLE_CONCRETE);
		edu.put("BLUE_CONCRETE", Material.BLUE_CONCRETE);
		edu.put("BROWN_CONCRETE", Material.BROWN_CONCRETE);
		edu.put("GREEN_CONCRETE", Material.GREEN_CONCRETE);
		edu.put("RED_CONCRETE", Material.RED_CONCRETE);
		edu.put("BLACK_CONCRETE", Material.BLACK_CONCRETE);
		edu.put("RED_CONCRETE", Material.RED_CONCRETE);
		edu.put("ORANGE_CONCRETE", Material.ORANGE_CONCRETE);
		edu.put("YELLOW_CONCRETE", Material.YELLOW_CONCRETE);
		edu.put("LIME_CONCRETE", Material.LIME_CONCRETE);
		edu.put("LIGHT_BLUE_CONCRETE", Material.LIGHT_BLUE_CONCRETE);
		edu.put("MAGENTA_CONCRETE", Material.MAGENTA_CONCRETE);
		edu.put("BIRCH_PLANKS", Material.BIRCH_PLANKS);
		edu.put("SPRUCE_PLANKS", Material.SPRUCE_PLANKS);
		edu.put("OAK_PLANKS", Material.OAK_PLANKS);
		edu.put("GRAY_CONCRETE", Material.GRAY_CONCRETE);
		edu.put("LIGHT_BLUE_STAINED_GLASS", Material.LIGHT_BLUE_STAINED_GLASS);
		edu.put("DIRT", Material.DIRT);
		edu.put("GRAY_CONCRETE", Material.GRAY_CONCRETE);
		edu.put("BROWN_MUSHROOM_BLOCK", Material.BROWN_MUSHROOM_BLOCK);
		edu.put("GRAY_CONCRETE", Material.GRAY_CONCRETE);



		Material value = (Material) edu.get(s);

		return value;

	}
}