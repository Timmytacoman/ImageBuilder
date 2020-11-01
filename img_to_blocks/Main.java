package me.timmytacoman.buildImage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin {

	@Override
	public void onEnable() {

		// getServer().getPluginManager().registerEvents(new Listeners(), this);

	}

	@Override
	public void onDisable() {

	}

	public static String getFirstLine() throws IOException {
		BufferedReader br = new BufferedReader(
				new FileReader("C:\\Users\\Timothy\\PycharmProjects\\misc_projects\\img_to_blocks\\block_data.txt"));

		String line = br.readLine();
		br.close();
		return line;
	}

	// ------------------------------------------------------------------------------------------------------------

	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {

		if (label.equalsIgnoreCase("build")) {
			if (sender instanceof Player) {

				Player player = (Player) sender;

				// find player location
				Location location = player.getLocation();

				// send message to server
				player.getServer().broadcastMessage(player.toString() + " is starting a build");

				// Get file generated from Python
				try {
					// load file
					String line = getFirstLine();

					// set y to feet level
					location.setY(location.getY() - 1);
					
					// get location constants
					float xloc = (float) location.getX();
					float zloc = (float) location.getZ();
					
					// create map to array for indexing
					String ar[] = line.split(", ");

					// read first element for width
					int width = Integer.parseInt(ar[0]);
					
					//read second element for height
					int height = Integer.parseInt(ar[1]);


					double total = width * height;
					

					
					int counter = 2;
					for (int y = 0; y < height; y++) { // height
						for (int x = 0; x < width; x++) { // width

							// find material
							Material m = Material.getMaterial(ar[counter]);
							System.out.println(ar[counter]);

							// find location
							location.setX(xloc + x);
							location.setZ(zloc + y);

							// place block
							location.getBlock().setType(m);
							
							// increment counter
							counter += 1;
							
							// send message
							double percent = (counter - 2) / total  * 100;
							System.out.println(String.valueOf(percent) + "% completed");

						}
					}

				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

			} else {
				sender.sendMessage("Not able to perform /build within console...");
				return true;

			}

		}

		return false;
	}

	// ------------------------------------------------------------------------------------------------------------

}
