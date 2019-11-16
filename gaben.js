const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)

    // List servers the bot is connected to
    console.log("Servers:")
    client.guilds.forEach((guild) => {
        console.log(" - " + guild.name)

        // List all channels
        guild.channels.forEach((channel) => {
            console.log(` -- ${channel.name} (${channel.type}) - ${channel.id}`)
        })
    client.on('message', msg => {
        if (msg.content === 'halflife3') {
        msg.reply('I\'m working on it!')
        }
    })
    })
})

client.on('message', (receivedMessage) => {
    if (receivedMessage.author == client.user) { // Prevent bot from responding to its own messages
        return
    }
    
    if (receivedMessage.content.startsWith("!")) {
        processCommand(receivedMessage)
    }
})

function processCommand(receivedMessage) {
    let fullCommand = receivedMessage.content.substr(1) // Remove the leading exclamation mark
    let splitCommand = fullCommand.split(" ") // Split the message up in to pieces for each space
    let primaryCommand = splitCommand[0] // The first word directly after the exclamation is the command
    let arguments1 = splitCommand.slice(1) // All other words are arguments/parameters/options for the command

    console.log("Command received: " + primaryCommand)
    console.log("Arguments: " + arguments1) // There may not be any arguments

    if (primaryCommand == "motd") {
        motdCommand(arguments1, receivedMessage)
    } else if (primaryCommand == "future") {
        futureCommand(arguments1, receivedMessage)
    } else {
        receivedMessage.channel.send("I don't understand the command. Try `!motd` or `!future`")
    }
}

function motdCommand(arguments1, receivedMessage) {
    if (arguments1.length == 0) {
        let longPanda = "```               ,,,\n```" +
                        "```             \'    \'/\\_/\\\n```" +
                        "```            \'       <@I@>\n```" +
                        "```<((((((((((  )____(  \\./\n```" +
                        "```           \\( \\(   \\(\\(\n```" +
                        "```            \`-\"\`-\"  \" \"   trashpandas\n```";
        receivedMessage.channel.send(longPanda)
    } else {
        receivedMessage.channel.send("Try `!motd`")
    }
}

function futureCommand(arguments1, receivedMessage) {
    if (arguments1.length < 2) {
        receivedMessage.channel.send("Not enough values to multiply. Try `!future 2 4 10` or `!future 5.2 7`")
        return
    }
    let product = 1
    arguments1.forEach((value) => {
        product = product * parseFloat(value)
    })
    receivedMessage.channel.send("The product of " + arguments1 + " multiplied together is: " + product.toString())
}

bot_secret_token = ""

client.login(bot_secret_token)
