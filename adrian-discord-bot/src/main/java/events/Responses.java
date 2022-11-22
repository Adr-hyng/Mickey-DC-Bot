package events;

import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class Responses extends ListenerAdapter {
	
	@Override
	public void onMessageReceived(MessageReceivedEvent event) {
		String messageSent = event.getMessage().getContentRaw();
		if(messageSent.equalsIgnoreCase("Adrian")) {
			event.getChannel().sendMessage("Meow!").queue();
		}
//		if(!event.isFromGuild()) return;
		
//		System.out.println(event.getMessage().getContentRaw());
	}
}
