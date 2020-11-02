package me.timmytacoman.buildImage;

import java.util.*;

import org.bukkit.Material;

public class dict {
	public static Material get_value(String s) {
		// Initializing a Dictionary
		Dictionary edu = new Hashtable();
		// put() method
		edu.put("1000", Material.STONE);
		edu.put("2000", Material.RED_WOOL);

		Material value = (Material) edu.get(s);

		return value;

	}
}