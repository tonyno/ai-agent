May 20, 2026

## Confluence \-\> GetOutline migration GO/NOGO \- Transcript

### 00:00:00

   
**Jan Barta:** information could actually tell us a lot. And I would when I how would I proceed like if we did this through like all the directions sharing quick learning strength first because I also like put some this is like the new scope that they asked for and this is some kind of like ideas from our site. So they can go through this, tell us which features they want and then we can I'm waiting for anybody else here. Let me start. So yes, but I like this. Denisa.  
**Tonda Kmoch:** Hello.  
**Jan Barta:** Hello.  
**Tonda Kmoch:** Give me a second.  
**Martin Klikar:** Hello.  
**Tonda Kmoch:** So, if you can guys wait for yourself and let's use Awesome. So we are probably all because or I'm not sure if Andy will join but yeah we discussed this topic like 50 times so I expect that you will not have anything else to say with Mati and Dennis. I believe that we are aligned as well. So let me share the screen. The reason why I wanted to have this meeting is that as you know and as was also mentioned on the all hands, we are in the process of transitioning from confluence to outline and I just wanted to make sure that we are like all aware of this like steps like what it exactly  
   
 

### 00:02:56

   
**Tonda Kmoch:** means because if there is time to potentially say no or like to say like hey there are like some concerns and so on probably the good timing is actually now because there are already some steps uh towards this migration that that are already in progress. So I wanted to have this meeting to share with you like where are we what are the potential like tradeoffs or or the risks so we are like all on the same page. How I would like to go through that is that as it there are like actually like a lot of topics that are that are happening. I don't want to go like super in detail with like everything because then we would potentially not make it in time. So if you will be like interested in anything just like shout the question and we can like discuss it or we can like discuss it offline. But uh yeah I wanted to just like mainly make sure that within those 30 minutes we cover everything. So uh let's start with like why we even like started with with like going with outline and uh the main reason is that we learned that like working with confluence and with AI is like super hard.  
   
 

### 00:04:07

   
**Tonda Kmoch:** So we are leveraging here the fact that outline is natively working uh with all the content in the way of MD files and MD files is exactly how AI is working. So in other words, outline is extremely well consumable by by AI. So working with AI and producing the output in outlining like it's like super easy because for AI it's not any outline. It's just those like MD files that that AI is extremely familiar with. So that was kind of let's say the the first uh trigger. Second trigger is that we had with Martin some like discussions about optimization of the costs of uh of the licenses. And actually one thing that that I am like quite happy about outline is that if we will agree today on this meeting that we will go with the open source version of the outline that means that every all the license costs are for free. So that's not only good for Martino like the budget that that it's free but for what is like super positive for me is that it will stop us from being like let's say careful who we invite to the space because whenever we discuss about inviting some stakeholders we always little bit tended to okay let's limit it let's maybe not invite everyone and so on what kind of let's say blocked that collaboration so this this will not be blocked like anymore because if we will go with open with open source if openl will tell us invite 50  
   
 

### 00:05:42

   
**Tonda Kmoch:** users we will say okay that's amazing let's invite 50 users no issue with that uh also as we use outline we see that it's also like much easier to use than like confluence because on confluence is obviously like super massive product with a lot of features a lot of complex configuration and so on here is everything like super easy it also supports the live collaboration so like people see what who is like editing what and so on. So yeah, we we believe that that it can be a great benefit for everyone. Just to be fair, on the other hand, outline is quite small product compared to out uh Confluent. So it doesn't have like so many features, so many plugins and so on. But we we are using this already for on few projects and we didn't come up to any limitations because yes if there are some limitation still the bigger tradeoff is the fact that the AI can extremely well work with with outline. So it's of course much easier to ask AI hey create me the preparation for that meeting put it to outline and like working with with this it's much better than that you are missing maybe some plug-in or like some some some feature uh so why we are having the discussion about the rollout now and what exactly is the question that that that we need to ask and discuss on on this meeting is that we already uh moved few projects to uh cloud instance of the of the  
   
 

### 00:07:18

   
**Tonda Kmoch:** outline and we are already working using that for a while but from security perspective this is not the correct like path so Honza already created the self-hosted instance in GCP so the plan is that we will use the get outline instance that is maintained by by Hanza and and is like fully under our control on on our our infrastructure And to this instance we need to uh we need to move uh all all the projects. So the decision that we will be discussing today is that the m about the migration of the whole company from confluence to this like self-hosted outline running that as a open source I will discuss it more in detail with that there are some like let's say tradeoffs or like some stuff that we need to be like all aware and uh and we will we will have like detailed uh we have the detailed plan for the migration itself that I will share with you in a moment. when it comes to projects that are impacted by this migration to to outline. So the situation is maybe much easier than it maybe might look like in from from the first glance because uh because we established already a rule that if the client has own tool we are using the the tools of the client.  
   
 

### 00:08:47

   
**Tonda Kmoch:** So for example on npm they have their own confluence they have their own jira. So this is absolutely not affected by this activity. Same on blackpoint. Blackpoint they have own their own confluence their own jira. So this is not like relevant to to to this activity. uh what is relevant is maybe for projects like for example open loop where we are on outline already uh on and mainly like EP that EP is still in our confluence and we will need to migrate them and the deal stage is in our confluence but actually they want to go potentially to their notion so potentially also this will not be part of of this project uh learning spring is already on on our outline anyway. So when it comes to projects, majority of them are already in the in the final solution. We just need to move it to this uh self-hosted solution. Uh so when it comes to pricing, uh Confluence uh cost six and a half dollars per user per month. Our goal or actually Hanza's suggestion uh is to go with the open source version because Hanza has also uh hands-on experience with using outline in his previous company when they were running that also on the self-hosted uh open source version and there were never any like issues.  
   
 

### 00:10:19

   
**Tonda Kmoch:** So that's why it's giving us the confidence that we can at least try try to to go this with this path. So that would mean that the cost for the license will be zero. Obviously there will be some costs for for the infrastructure that that Hanza is estimating but very likely it will not be anything crazy. I'm not sure if you have already any estimations but yeah so far basically any any  
**Michaela Mlynarcikova:** source which costs some meaningful amount of money is the database and it's like $150 per month and that's the only thing which costs something really the storage the network it's nothing it's like sense so instead  
**Tonda Kmoch:** of paying like now we are paying like uh 800 900 we will be paying like around like few hundreds for for the database and obviously the huge advantage is that we will have everything under our control it's also like open source So potentially we can uh use it like V coding doing some like changes or like integrations and so on. Also uh outline has like huge amount of web hooks.  
   
 

### 00:11:28

   
**Tonda Kmoch:** So if we want to react on like different events that I don't know user is created or collection is created and so on we can like plug it to some like automations. So with the open source version there are like few things that are missing in the open source version and we already went through that with with Hanza to make sure that we will not miss anything. So I will maybe mention only like few of these points. So Hanza was already discussing with Martin right that uh we will go with the two-actor authentification of the Google. So everything will be happening through Google where we have the two-factor authentification. So we will not need two factor authentification of the outline because that would be actually not two factor that would be third factor that would be already like uh much more than uh than our internal policies uh requires.  
**Martin Klikar:** Can I have a question here on this one?  
**Tonda Kmoch:** Uh  
**Michaela Mlynarcikova:** H.  
**Martin Klikar:** Um, so,  
**Tonda Kmoch:** yes.  
**Martin Klikar:** uh,  
**Michaela Mlynarcikova:** So,  
**Martin Klikar:** can we enforce the fact that people can only log in or register through Google?  
   
 

### 00:12:36

   
**Martin Klikar:** Um, is it not possible for them to add login name and password manually?  
**Tonda Kmoch:** Uh yeah that's great question. I think it's uh yeah I think that there is the configuration for that. I will just like double check that but there is not even any uh place where to actually put any login. It's just showing you the button for the uh Google login.  
**Martin Klikar:** Because for me when you send that link uh it offered me two options either Google option or name and password option.  
**Tonda Kmoch:** Okay. So, I didn't see that. So, sorry. I will I will check it. But I think that I saw it in the administration that it was feasible to turn it off.  
**Andy Powell:** the the only challenge will be if we have uh clients logging in that aren't on Google. So So that may not work.  
**Tonda Kmoch:** Yes.  
**Andy Powell:** So yeah. Um but I think I think we can like take this and solve it separately right on  
**Tonda Kmoch:** Or we can maybe yeah check it in the database like periodically that no one is using  
   
 

### 00:13:31

   
**Andy Powell:** the  
**Tonda Kmoch:** that for example in some like different way. But uh great great point Martin. I will I will take it and uh make sure that that we have this turned on.  
**Andy Powell:** can I maybe just ask one more question because yeah I haven't actually dived to the details of this before.  
**Martin Klikar:** Mhm.  
**Andy Powell:** So Hanza, when you were using it at your previous company, could you maybe just describe a little bit like the let's say the scale of that, like number of users,  
**Tonda Kmoch:** Yeah,  
**Andy Powell:** like how often you're using it?  
**Tonda Kmoch:** I think Yeah, I think it was very  
**Michaela Mlynarcikova:** very close to oaks. Uh could be 120 150 users. Uh probably less collections potentially. Uh but I think scale was very very similar. We have been using it for roughly two years, one and a half maybe something like that. And yeah, as TA mentioned, we haven't really hit any issues to be honest with it. Uh like a single one. Uh it was all working, you know, very well.  
   
 

### 00:14:39

   
**Michaela Mlynarcikova:** Awesome. So,  
**Tonda Kmoch:** Probably the only like feature that was like making us a little bit nervous is that the Confluence importer is a paid uh feature. But Hanza found a solution and he already is in process of migrating the stuff through like his like local version and so on. So this doesn't seem to be something that we would actually need to pay for wizard. Well, you are the uh  
**Cristina Attina:** Thank you.  
**Tonda Kmoch:** so one thing that  
**Martin Klikar:** And maybe maybe sorry for uh what what about that guest  
**Tonda Kmoch:** Yes.  
**Martin Klikar:** account? Um I just quickly read through  
**Tonda Kmoch:** Yeah. Yes. Yes.  
**Martin Klikar:** the  
**Tonda Kmoch:** So, so uh outline has a feature that user can be a guest. Guest means that you will not automatically get permission like anywhere and you will get permission only there where you are explicitly set to get the permission. That's the feature of guest accounts and we will not need that because we will kind of let's say he hack it or like overcome that by fact that first we will not allow anyone to create a new collections.  
   
 

### 00:15:56

   
**Tonda Kmoch:** It will be just Misha or me like it will be like controlled. So it will not happen this like mirror situation that someone did something that that didn't know what he's doing. And whenever we will create a new collection, we will never give the permission to that collection to all users but we will give the permission only to specific groups. So by that you are we are like fully overcoming this uh this challenge with missing guest  
**Martin Klikar:** Okay.  
**Tonda Kmoch:** accounts  
**Martin Klikar:** And the collection that that means like project like a  
**Andy Powell:** and  
**Tonda Kmoch:** collection is project.  
**Martin Klikar:** new Yeah.  
**Tonda Kmoch:** Yes.  
**Michaela Mlynarcikova:** Yeah.  
**Martin Klikar:** Yeah.  
**Tonda Kmoch:** Yes.  
**Martin Klikar:** Okay. Okay. Okay. Makes  
**Andy Powell:** and maybe how do you because then all of the risk is then on how those groups are managed,  
**Martin Klikar:** sense.  
**Andy Powell:** right? So so I guess we should all is there a sorry to dive to the detail but I see that as a risk. So will we somehow manage it so that only certain people can manage group access?  
   
 

### 00:16:49

   
**Tonda Kmoch:** Yes. Yes.  
**Andy Powell:** Amazing.  
**Tonda Kmoch:** Yes. Outline has a feature that even the some of the people can manage the group like themselves. But this we will turn off and it will be managed by Misha because well yeah there are no like many changes right if we have people in correct groups then everything works fine so one thing that I just wanted to mention just like for the transparency I don't believe that it's actually like huge issue but I just wanted to highlight that by the fact that we are self-hosting the solution that means that someone within the company needs to have the access to the raw database and like everything. So in our Confluence for example, even Jake cannot access my personal stuff that I put for example to Confluence. But that would not be true anymore with any self-hosted solution. So it's not about outline, it's more like about the fact of self-hosting. What means that obviously the administrator or someone who is managing that infrastructure has technically access to the database and has technically the ability to go to the database and like check some data.  
   
 

### 00:18:03

   
**Tonda Kmoch:** So that means that probably super sensitive information where we would like have concerns that it should not be visible for example for Hanza for whatever reasons potentially this content we should not put to to outline because yeah if Hanza goes crazy and we'll start like exploring that technically he can do that. May maybe we could also  
**Michaela Mlynarcikova:** around that. around that. Uh I don't know because like the the there is technically no maintenance needed on the outline. We will probably update the version once a month or so or whatever. Maybe we could I don't know give access to the database just to Theo or something and I could do the the maintenance with him once a month. So I can imagine a solution how to get around it because I mean I I don't expect village to need to do anything about the outline once it's running.  
**Cristina Attina:** hopeful. I mean, of  
**Michaela Mlynarcikova:** Of course I could be wrong but I think you could get around that as Yeah, I would suggest to that  
   
 

### 00:19:03

   
**Tonda Kmoch:** for three months definitely it should be on Hanza and it's maybe easier not to put there like something that must be super super super private but then I agree once it will be like super stable it's maybe great idea for example to do this so I put here like some suggestions and we can like discuss it on some like other meeting what potentially to do about  
**Martin Klikar:** Yeah. So Hanza then I think that if you'll be work like working from your like Gmail account, it should probably not be the regular one, right? It should be the admin admin  
**Tonda Kmoch:** I would  
**Martin Klikar:** one.  
**Michaela Mlynarcikova:** Uh yeah, we can think about it.  
**Tonda Kmoch:** question.  
**Michaela Mlynarcikova:** Maybe admin is better.  
**Tonda Kmoch:** So and we can discuss it like offline. It's it's more like I don't believe that this is the blocker for the whole roll out at all. So I just wanted to make it for your attention.  
**Martin Klikar:** Yeah.  
**Tonda Kmoch:** So then uh one note about working with with outline and working with collection. So in outline a project is called collection.  
   
 

### 00:20:12

   
**Tonda Kmoch:** In Confluence it was it used to be called space. The idea is that on the project level, collection level, the permission will be only to the project team as as you were Martin asking. So not for the whole company, only the project team potentially also like the or like probably to the DMT and execs and then somewhere in that nested folder there will be some  
**Martin Klikar:** Yes.  
**Tonda Kmoch:** subfolder that will be shared also with the client but only like some subsets. So for example, meetings will not be shared with the client because obviously there there can be some like raw data blah blah blah. Uh but only like selected subset what will be exactly the name of the folder and structure and so on is to be like defined. I just wanted to share it more here like from the like permission perspective. So people will be splitted to group uh to the projects through the groups and they will have access only to those projects that they are working on plus digital management team and execs will see all the projects.  
   
 

### 00:21:22

   
**Tonda Kmoch:** Uh yeah here I have like technical detail like how to actually like achieve that and that I will go with with Misha in uh in in detail. Also as I mentioned we will not be using the group admin and so on. Uh so now more on the migration plan. So from confluence we are about to migrate probably just around 20 spaces. What is amazing because we have 200 spaces there. So only like 20 are relevant and we created this plan of of the migration. So we already went through the phase one uh phase zero when we tried get outline on selected projects and we were running that on the this cloud hosted solution. So this is already done today. We migrated to the final outline this from honzaf this like self-hosted uh openloop intake and openloop rcm. We will also migrate few more content from from Confluence as like let's say first wave to just like check that everything is working fine and the idea is that by Monday we would like to know if everything is running well or not and if yes then we will uh start migrating all the remaining stuff and we will also uh uh uh we will also migrate the the uh yeah the the non-living like confluence projects like I don't know narwhal swiftly and and so on those that are more there like for like saving perspective but they are not being touched like every day and then uh in uh on on on Monday so this sorry this phase two we would like to start doing like today  
   
 

### 00:23:19

   
**Tonda Kmoch:** uh if if we will not get any like let's say no go from from you and the idea is that on Monday we will we will have the feedback from intake we will have the feedback from from like RCM we will see how that migration of narwhal and swiftly these non super important uh projects in confluence that are already done how it went if everything was uh transferred correctly and so on and then that means that uh we will move to the phase three when we will actually cut over and like move those uh remaining living documents to uh uh to outline what will happen probably uh yes definitely like outside working hours so I don't know potentially in on Sunday like in two weeks from from now everything like let's say triggered or uh by by the result of this like phase two and this we will discuss with you definitely like much more in detail and mainly with those projects that uh that are impacted Uh the goal like is  
**Martin Klikar:** And can I just one quick?  
**Tonda Kmoch:** that  
**Martin Klikar:** Yeah. Yeah, I just have one quick question.  
   
 

### 00:24:31

   
**Martin Klikar:** Uh for the projects that we are going to archive, I mean by the way that's that's good point.  
**Tonda Kmoch:** sorry  
**Martin Klikar:** I wanted to just raise that that we should have for the projects where it's not that long that we finished it. We might need to keep some documentation as some evidence in case we can we get some conflict with some clients.  
**Cristina Attina:** Yeah.  
**Martin Klikar:** Um which is good that you included that and who will get access to that just like ex and DMT  
**Tonda Kmoch:** So,  
**Martin Klikar:** again.  
**Tonda Kmoch:** so the idea is that this point 9.4 is that uh as confluence is being paid by user not by the content we will keep everything in confluence we will just restrict the amount of users. So all the execs all the DMT will have access still to these 200 spaces that we have in confluence. We will just have it for the yeah for the as as this like let's say backup if we will find out that  
**Martin Klikar:** Yeah.  
**Tonda Kmoch:** anything is missing in outline and so on.  
   
 

### 00:25:27

   
**Tonda Kmoch:** So we will be able to migrate that potentially later.  
**Martin Klikar:** Makes  
**Tonda Kmoch:** Okay. And also we will let's say in one month cut off and remove  
**Martin Klikar:** sense.  
**Tonda Kmoch:** this old get outline that we are running in in cloud probably let's say one month after the migration because some of the external clients are having the accesses to to that like old instance obviously we don't want to change it like super quickly uh And yeah, we have last five minutes. So yeah, I will maybe like pause here and yeah, mainly like ask if anyone sees like any like issues or like anything why we should like potentially like stop or like pause this activity. No, makes a lot of sense. Thank you for all your hard work on  
**Cristina Attina:** I love it.  
**Tonda Kmoch:** that.  
**Cristina Attina:** Let's move  
**Martin Klikar:** Um I I have one question about uh just just maybe maybe a stupid one.  
**Cristina Attina:** forward.  
**Martin Klikar:** What does it mean that it's open source? Um I mean I I kind of understand that if we self-host it ourselves, it's secure.  
   
 

### 00:26:38

   
**Martin Klikar:** No one can enter it you know from cloud no one get outline site is going to get access um so only if you have an account or if you break into account of someone from slap you can access but uh does it have any implication that it's out like open source Yes.  
**Tonda Kmoch:** So, Go back in.  
**Michaela Mlynarcikova:** Ally what does it mean is that there are essentially two versions of outline. One is closed source and that's what they are running on that software as a service version and that's technically what you can also run if you have the enterprise key and pay for the license for that you essentially don't have the source code and you kind of I mean  
**Martin Klikar:** Mhm.  
**Michaela Mlynarcikova:** you take the word of the vendor that it's secure and whatever is there is there and stuff like that and then there's the open source version which is just publicly available on GitHub anybody can download it anybody anybody can contribute to it. Anybody can you know change it on their own and that's what we are running. So basically uh the the practical implications is that we essentially rely on the community uh who manages and maintains the open source version that it's secure that it run that it's that it runs well uh etc etc think I mean it s it could sound let's say scary a bit but at the same time uh the version is very actively maintained what it means that they're like you know update ates or changes being done on pretty much like daily basis for I think like  
   
 

### 00:28:12

   
**Michaela Mlynarcikova:** three three years now. That's good because you know the the the solution will get you know security updates by the community and everything. Uh so yeah kind of that's what it means if that answer the question and how is  
**Andy Powell:** I think  
**Michaela Mlynarcikova:** it in conflictation?  
**Cristina Attina:** And conference is private product owned  
**Michaela Mlynarcikova:** Nobody has a code for that.  
**Cristina Attina:** by  
**Michaela Mlynarcikova:** So it's kind of similar for that um private enterprise version  
**Cristina Attina:** default.  
**Andy Powell:** maybe to maybe to like Martin in your point,  
**Michaela Mlynarcikova:** of  
**Andy Powell:** does it make sense to do any let's say and I'm more asking you for advice here some kind of like pen testing or like security testing of this product in the same way that we would if we releasing a client product, right? Because yes, we should rely on open source, but we should also we can rely on it to some extent, but should we also do something on our side to let's say just validate?  
**Tonda Kmoch:** Of  
**Andy Powell:** What do you think, Ton Hanza?  
   
 

### 00:29:09

   
**Michaela Mlynarcikova:** Yeah.  
**Andy Powell:** I I don't  
**Michaela Mlynarcikova:** Well, yeah.  
**Tonda Kmoch:** course. Yeah. Of course. The answer is yes. The problem is that those tests are not cheap and they are also like quite often like let's say very s\*\*\* like it's just it's just to have that like signature.  
**Andy Powell:** s\*\*\*.  
**Tonda Kmoch:** So maybe instead of potentially doing this, what we can do especially if someone will be like on bench is to like using some like VIP  
**Andy Powell:** He  
**Tonda Kmoch:** coding and like some like OASP like like methodology or like rules try to like understand that at least like ourselves like how it really like works to really like investigate like how it works with users and so on. So yeah. So, so Woodro being  
**Michaela Mlynarcikova:** another sort of like a mini hackathon. We we we we we basically ask people to break it essentially. Uh we put their I don't know whatever 1,000 prize money voter to vault or whatever whoever finds the most issues with it. Uh, and we do like a interm something like what you were saying essentially, but we could do it like a fun way.  
   
 

### 00:30:14

   
**Michaela Mlynarcikova:** Not somebody who's on a bench, but really kind of go for it, guys. Kind of try to hang in  
**Martin Klikar:** Yeah, because the Yeah, the you know my only follow-up question would be whether like like usually you know you do rely on open source without any future testing. think. Yeah. So, I mean,  
**Michaela Mlynarcikova:** There we go.  
**Martin Klikar:** because I don't I don't technically understand it. I'm just raising that and probably I'll rely on you, Hanza, because like you you work with the code the most and and if you think it's it's it's secure for the all the documentation that we'll have there about our clients, um then I have no issues with that.  
**Michaela Mlynarcikova:** Yes, I think it is secure obviously at the same time I'm the one who is basically running it. So I'm definitely uh uh the the weak link in the chain 100%. So I I I agree with basically and on that it would make sense definitely to to do some sort of u testing hardening whatever and we can discuss however that would look like if it makes sense to pay somebody external if we can do it internally I think there are multiple options I would do at least couple of them or one of them or we can do some VPN IA.  
   
 

### 00:31:40

   
**Tonda Kmoch:** and right but obviously no probably no one wants to use some VPN but that would solve it as well right but I I also wouldn't kind  
**Michaela Mlynarcikova:** have this as a as a deal breaker right now. So I would also put it on the backlog of let's say things to do. Uh but I I wouldn't be uh afraid of the open source per se.  
**Martin Klikar:** Mhm. Mhm.  
**Tonda Kmoch:** I just have one point. I would love to see Christina.  
**Martin Klikar:** Okay.  
**Cristina Attina:** you put together the like the company documentation. I just want to make sure everything's there and we uh we use it as a chance to just  
**Michaela Mlynarcikova:** Hey,  
**Cristina Attina:** clean it up and have less less less documentation but just the most important things. So, so are you accountable for like setting up the  
**Tonda Kmoch:** documentation.  
**Cristina Attina:** company?  
**Tonda Kmoch:** What I mean by complete documentation  
**Cristina Attina:** General information on Oaks Lab, how we're set up, how we run the company, those are under the people part and uh and um uh the  
   
 

### 00:32:48

   
**Michaela Mlynarcikova:** The company newsletter.  
**Cristina Attina:** news and anything for onboarding. Yep. So, if once you create that, please just share it with me. I can give you my feedback. Oh, and then general policies that we have. Yeah. So actually for  
**Tonda Kmoch:** this people department can be if we will agree with Christina in actually this bench that we will start migrating like immediately because that's probably not something that is like changing every day so we can like froze it in in confluence migrate that check it if it's like everything fine and then start using that already in outline Perfect. I would love to do that. And I would put it under I would move it away from the  
**Cristina Attina:** department and I would just have the oaks lab what are we what is it called the group is it or what's the collection and then all the information there so  
**Tonda Kmoch:** collection.  
**Andy Powell:** Yeah.  
**Cristina Attina:** let me know once I can check it yep awesome  
**Andy Powell:** Yeah. And I just think at some point there should be some action somewhere just to like look at how we organize those collections more from like a visual point of view than anything like a kind of UX  
   
 

### 00:33:47

   
**Michaela Mlynarcikova:** Yeah.  
**Andy Powell:** thing because I think the one downside to outline full transparency for everyone who's going to use it for the first time is because it's just a list on the left hand side of those collections the hierarchy is a little bit harder to discern than in Confluence. That's the only downside.  
**Cristina Attina:** Good job.  
**Andy Powell:** So if you are in lots of collections, it's kind of hard to like navigate yourself. So we probably need to give people some guidance on how to do it. It's just not quite as clear as Confluence, but I'm sure we can figure it out.  
**Cristina Attina:** Yeah, we can then review it all together.  
**Tonda Kmoch:** We should not have like 20 collections.  
**Cristina Attina:** Yeah,  
**Tonda Kmoch:** Yeah.  
**Andy Powell:** Yeah.  
**Martin Klikar:** It's  
**Tonda Kmoch:** Everyone should have maximum like five for example. And by default, everybody gets the connection. Yes,  
**Cristina Attina:** exactly.  
**Martin Klikar:** Antonio,  
**Tonda Kmoch:** exactly.  
**Martin Klikar:** did you solve the labels with Marquetta?  
**Tonda Kmoch:** Uh so I think that she was writing that she needs to speak with you. I think that it was last last  
**Martin Klikar:** Okay. So,  
**Tonda Kmoch:** date.  
**Martin Klikar:** she spoke to me, but then she was supposed to go to you.  
**Tonda Kmoch:** Oh, okay. So I need to check I will check it. I will check it.  
**Martin Klikar:** Yeah. Cool. Okay. Sounds good.  
**Tonda Kmoch:** Thank you. See you. See you. Have a nice day.  
**Martin Klikar:** Thank you. Bye.  
   
 

### Transcription ended after 00:35:11

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*