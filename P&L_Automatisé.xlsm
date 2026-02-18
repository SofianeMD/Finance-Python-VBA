Sub CalculerPL_Automatique()
    Dim wsPtf As Worksheet
    Dim wsCarnet As Worksheet
    Dim lastRow As Long
    Dim i As Long
    Dim ticker As String
    Dim cours As Variable
    Dim prixAchat As Double
    Dim quantite As Long
    
    Set wsPtf = ThisWorkbook.Sheets("Portefeuille")
    Set wsCarnet = ThisWorkbook.Sheets("Carnet")
    
    ' Trouver la dernière ligne du ptf
    lastRow = wsPtf.Cells(wsPtf.Rows.Count, "A").End(xlUp).Row
    
    For i = 2 To lastRow
        ticker = wsPtf.Cells(i, 1).Value
        quantite = wsPtf.Cells(i, 2).Value
        prixAchat = wsPtf.Cells(i, 3).Value
        
        On Error Resume Next        
        ' On va chercher le prix actuel dans le carnet
        cours = Application.WorksheetFunction.VLookup(ticker, wsCarnet.Range("A:B"), 2, False)
        On Error GoTo 0

        If cours > 0 Then
            wsPtf.Cells(i, 4).Value = cours
            
            wsPtf.Cells(i, 5).Value = quantite * (cours - prixAchat)
            
            ' Pour être plus lisible  on rajoute des couleurs.
            If wsPtf.Cells(i, 5).Value >= 0 Then
                wsPtf.Cells(i, 5).Font.Color = RGB(0, 128, 0)
            Else
                wsPtf.Cells(i, 5).Font.Color = RGB(255, 0, 0)
            End If
        End If
        
        cours = 0
    Next i
    
End Sub

Dim Maj As Date
Sub DemarrerUpdate()
    ' Lance la macro de calcul du P&L
    Call CalculerPL_Automatique
    
    ' Programme la prochaine actualisation
    Maj = Now + TimeValue("00:01:00")
    Application.OnTime Maj, "DemarrerUpdate"
    
    ' Ajouter l'heure de la dernière MAJ
    Sheets("Dashboard").Range("B1").Value = "Dernière MAJ : " & Now
End Sub

Sub ArreterUpdate()
    ' Pour arrêter la boucle proprement
    On Error Resume Next
    Application.OnTime Maj, "DemarrerUpdate", , False
End Sub
