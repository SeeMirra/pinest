def DrawGraph():
        global MaxTemp
        global LastTemps
        global LastHumids
        global LastHeatings

        surface = pygame.Surface((300,300))
        GraphBottom =220
        GraphRight = 60
        GraphMaxRight = 360
        GraphMaxHeight = 160
        PrevPoint = (60,60)
        PrevHumid = (60,60)
        PrevHeat = (60,60)
        PrevValue = 0
        HumidTopAdjust = (GraphMaxHeight) / 100
        PointLeftAdjust = (GraphMaxRight - GraphRight) / 288
        PointTopAdjust = (GraphMaxHeight) / MaxTemp
        for i in range(0,288):

                if(len(LastTemps) > 0):
                        if(i == 0):
                                #print HERE
                                PrevPoint = (GraphRight +(PointLeftAdjust * i),GraphBottom -(PointTopAdjust* LastTemps[i]))
                        elif(i < len(LastTemps)):
                                #print HERE2
                                pygame.draw.line(surface, (255,0,0), PrevPoint, (GraphRight +(PointLeftAdjust * i),GraphBottom -(PointTopAdjust* LastTemps[i])),1)
                                PrevPoint = (GraphRight +(PointLeftAdjust * i),GraphBottom -(PointTopAdjust* LastTemps[i]))
        for i in range(0,288):
                if(len(LastHumids) > 0):
                        if(i ==0):
                                PrevHumid = (GraphRight + (PointLeftAdjust * i),GraphBottom - (HumidTopAdjust * LastHumids[i]))
                        if(i < len(LastHumids)):
                                pygame.draw.line(surface, (0,0,255), PrevHumid, (GraphRight +(PointLeftAdjust * i),GraphBottom -(HumidTopAdjust* LastHumids[i])),1)
                                PrevHumid = (GraphRight +(PointLeftAdjust * i),GraphBottom -(HumidTopAdjust* LastHumids[i]))
        for i in range(0,288):
                PointValue = 0;
                if(len(LastHeatings) > 0):
					if( i < len(LastHeatings)):
						if(LastHeatings[i] == 0):
							PointValue = 160
						else:
							PointValue = 10
						if(i == 0):
							PrevHeat = (GraphRight, GraphBottom - PointValue)
							PrevValue = PointValue
						else:

								if(PrevValue == PointValue):
										pygame.draw.line(surface, (0,255,0), PrevHeat, (GraphRight + (PointLeftAdjust * i), GraphBottom - PointValue))
										PrevHeat = (GraphRight + (PointLeftAdjust * i), GraphBottom - PointValue)
								else:
										pygame.draw.line(surface, (0,255,0), (GraphRight + (PointLeftAdjust * i), GraphBottom - PointValue), (GraphRight + (PointLeftAdjust *i), GraphBottom - PrevValue))
										PrevHeat = (GraphRight + (PointLeftAdjust * i), GraphBottom - PointValue)
								PrevValue = PointValue
        pygame.draw.line(surface, (255,255,255), (60,60), (60, 220), 1)
        pygame.draw.line(surface, (255,255,255), (60,220), (350,220),1)
        smallfont = pygame.font.Font(None, 15)
        SmallText = smallfont.render(`MaxTemp`,1, (255,0,0))
        surface.blit(SmallText,(45,55))
        SmallText = smallfont.render('100',1, (0,0,255))
        surface.blit(SmallText,(40,65))
        SmallText = smallfont.render(`int(MaxTemp / 2)`,1, (255,0,0))
        surface.blit(SmallText,(45,135))
        SmallText = smallfont.render('50',1, (0,0,255))
        surface.blit(SmallText,(40,145))
        SmallText = smallfont.render('0',1,(255,0,0))
        surface.blit(SmallText,(50,215))
        SmallText = smallfont.render('0',1,(0,0,255))
        surface.blit(SmallText,(47,225))
        SmallText = smallfont.render('0',1,(255,255,255))
        surface.blit(SmallText,(60,225))
        SmallText = smallfont.render('-12Hours',1,(255,255,255))
        surface.blit(SmallText, (145,225))
        SmallText = smallfont.render('-24Hours',1,(255,255,255))
        surface.blit(SmallText, (260,225))
        return surface
