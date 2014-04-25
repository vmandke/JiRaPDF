import uno
 
# a UNO struct later needed to create a document
from com.sun.star.text.ControlCharacter import PARAGRAPH_BREAK
from com.sun.star.text.TextContentAnchorType import AS_CHARACTER
from com.sun.star.awt import Size 
from com.sun.star.lang import XMain




class PrintToWriter:

       def __init__( self ): 
       	
       	self.localContext = uno.getComponentContext()
       	self.resolver = self.localContext.ServiceManager.createInstanceWithContext(
       				"com.sun.star.bridge.UnoUrlResolver", self.localContext )
       	self.ctx = self.resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
       	self.smgr = self.ctx.ServiceManager
       	self.desktop = self.smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",self.ctx)
       	self.doc = self.desktop.loadComponentFromURL( "private:factory/swriter","_blank", 0, () )
       	self.model = self.desktop.getCurrentComponent()
       	self.text = self.model.Text
       	self.cursor = self.text.createTextCursor()
        self.tableStyle("BLUE") #default color scheme is Blue


       def insertTextIntoCell(self, table, cellName, text, color ):
           tableText = self.table.getCellByName( cellName )
           cursor = tableText.createTextCursor()
           cursor.setPropertyValue( "CharColor", color )
           tableText.setString( str(text) )

           if (str(text).strip().startswith("http")):
           	cursor.gotoStart(False)
           	cursor.gotoEnd(True)
           	cursor.HyperLinkURL = str(text).strip()

           elif (str(text).strip().startswith("LIB-")):
           	cursor.gotoStart(False)
           	cursor.gotoEnd(True)
           	cursor.HyperLinkURL = "https://synerzip.atlassian.net/browse/" + str(text).strip()

       
       def insertTextInRow(self, rowIndex, textList):
       	    index = "A" + str(rowIndex)
       	    for text in textList:
       	        self.insertTextIntoCell( self.table, index, text, 0 )
       	        index = chr(ord(index[0]) + 1) + str(rowIndex)


       def initTable(self, rows,cols, headings):
           self.table = self.doc.createInstance( "com.sun.star.text.TextTable" )
           self.table.initialize( rows +1 ,cols)
           self.text.insertTextContent( self.cursor, self.table, 0 )
           rows = self.table.Rows	 
           self.table.setPropertyValue( "BackTransparent", uno.Bool(0) )
           self.table.setPropertyValue( "BackColor", self.TablebackColor )
           row = rows.getByIndex(0)
           row.setPropertyValue( "BackTransparent", uno.Bool(0) )
           row.setPropertyValue( "BackColor", self.HeadingRowColor )
           textColor = 16777215
           self.text.insertControlCharacter(self.cursor, PARAGRAPH_BREAK, 0)
           index = "A1"
           for heading in headings:
       	       self.insertTextIntoCell( self.table, index, heading, textColor )
       	       index = chr(ord(index[0]) + 1) + str(1)
       
       def insertHeading(self,string, paraStyleName):
       	   self.cursor.ParaStyleName = paraStyleName
       	   self.text.insertString(self.cursor, str(string), 0)
           self.text.insertControlCharacter(self.cursor, PARAGRAPH_BREAK, 0)
       	   self.cursor.ParaStyleName = "Standard"

       def insertParaBreak(self):
          self.text.insertControlCharacter(self.cursor, PARAGRAPH_BREAK, 0)

       def tableStyle(self, color):
           if color == "PURPLE":
              self.TablebackColor = int("EDE6F2", 16)
              self.HeadingRowColor = int("75508F", 16)

           elif color == "GREEN":
              self.TablebackColor = int("EDF7EE", 16)
              self.HeadingRowColor = int("3F6943", 16)

           elif color == "RED":
              self.TablebackColor = int("FCEEEA", 16)
              self.HeadingRowColor = int("E87758", 16)

           elif color == "ORANGE":
              self.TablebackColor = int("F9FAD5", 16)
              self.HeadingRowColor = int("FAB452", 16)

           elif color == "BLUE":
              self.TablebackColor = int("DAE3EB", 16)
              self.HeadingRowColor = int("5A90C7", 16)

           elif color == "GREY":
              self.TablebackColor = int("F2EFEF", 16)
              self.HeadingRowColor = int("7D7D7D", 16)
