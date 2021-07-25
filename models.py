from .app import db


class ADP(db.Model):
    __tablename__ = 'ADP_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.bigint)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
    AuctionValue = db.Column(db.integer)
    AuctionValuePPR = db.Column(db.integer)
    AverageDraftPositionIDP = db.Column(db.double)
    AverageDraftPositionRookie = db.Column(db.double)
    AverageDraftPositionDynasty = db.Column(db.double)
    AverageDraftPosition2QB = db.Column(db.double)
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name) 
class DEF(db.Model):
    __tablename__ = 'DEF_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.intger)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
    
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name) 
class K(db.Model):
    __tablename__ = 'K_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.integer)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
    
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name) 
class Position_Dropdown(db.Model):
    __tablename__ = 'Position_dropdown'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.integer)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
   
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name) 
class QB(db.Model):
    __tablename__ = 'QB_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.bigint)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)

    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name) 
class RB(db.Model):
    __tablename__ = 'RB_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.integer)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
  
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name)
class TE(db.Model):
    __tablename__ = 'TE_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.integer)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
    
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name) 
class WR(db.Model):
    __tablename__ = 'WR_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.integer)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
    
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name)
class Highlights(db.Model):
    __tablename__ = 'Adp_Data'
    FantasyPlayerKey = db.Column(db.string, primary_key=True)
    PlayerID = db.Column(db.integer)
    Name = db.Column(db.string)
    Team = db.Column(db.string)
    Position = db.Column(db.string)
    AverageDraftPosition = db.Column(db.double)
    AverageDraftPositionPPR = db.Column(db.double)
    ByeWeek = db.Column(db.double)
    LastSeasonFantasyPoints =db.Column(db.double)
    ProjectedFantasyPoints = db.Column(db.double)
    
    def __repr__(self):
        return '<ADP_DATA %r>' % (self.name)

class BoxPlot(db.Model):
    __tablename__ = 'BoxPlot'
    NAME = db.Column(db.string, primary_key=True)
    POSITION = db.Column(db.string)
    PROJECTE_POINTS = db.Column(db.double) 


    def __repr__(self):
        return '<Pet %r>' % (self.name)
