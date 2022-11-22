package discord.bot;

import javax.security.auth.login.LoginException;

import events.Responses;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;

public class AdrianBot {
	public static void main(String[] args) throws LoginException {
		JDA bot = JDABuilder.createDefault("MTA0NDYyNTA0ODY3OTQ4MTQ1NA.Gda22U.mFw7yFfXxy0YDiVZRgo5FWNmx5JSdqkAZv5-tU")
				.setActivity(Activity.playing("with your mom"))
				.enableIntents(GatewayIntent.MESSAGE_CONTENT)
				.build();
		
		bot.addEventListener(new Responses());
	}
}
