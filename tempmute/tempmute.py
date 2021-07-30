@client.command()
@commands.has_any_role(853285815638294558, 812513312574144522, 791514339546103808, 793276858870530069, 751489493512617994, 653983672189452288, 832008780639109120)
async def tempmute(ctx, member : discord.Member, time=0,*, reason=None):
    if not member or time == 0 or time == str:
        await ctx.channel.send(embed=commanderror)
        return
    elif reason == None:
        reason = "No Reason Provided"

    muteRole = discord.utils.get(ctx.guild.roles, id=663076470180151339)
    await member.add_roles(muteRole)

    tempMuteEmbed = discord.Embed(colour=embedcolour, description=f"**Reason:** {reason}")
    tempMuteEmbed.set_author(name=f"{member} Has Been Muted", icon_url=f"{member.avatar_url}")
    tempMuteEmbed.set_footer(text=embedfooter)

    await ctx.channel.send(embed=tempMuteEmbed)

    tempMuteModLogEmbed = discord.Embed(color=embedcolour)
    tempMuteModLogEmbed.set_author(name=f"[MUTE] {member}", icon_url=f"{member.avatar_url}")
    tempMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    tempMuteModLogEmbed.add_field(name="Moderator", value=f"{ctx.message.author}")
    tempMuteModLogEmbed.add_field(name="Reason", value=f"{reason}")
    tempMuteModLogEmbed.add_field(name="Duration", value=f"{str(time)}")
    tempMuteModLogEmbed.set_footer(text=embedfooter)
    modlog = client.get_channel(638783464438759464)
    await modlog.send(embed=tempMuteModLogEmbed)

    tempMuteDM = discord.Embed(color=embedcolour, title="Mute Notification", description="You Were Muted In **The Official Vanmanyo Discord Server**")
    tempMuteDM.set_footer(text=embedfooter)
    tempMuteDM.add_field(name="Reason", value=f"{reason}")
    tempMuteDM.add_field(name="Duration", value=f"{time}")

    userToDM = client.get_user(member.id)
    await userToDM.send(embed=tempMuteDM)

    await asyncio.sleep(time)
    await member.remove_roles(muteRole)

    unMuteModLogEmbed = discord.Embed(color=embedcolour)
    unMuteModLogEmbed.set_author(name=f"[UNMUTE] {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    unMuteModLogEmbed.set_footer(text=embedfooter)
    modlog = client.get_channel(638783464438759464)
    await modlog.send(embed=unMuteModLogEmbed)
