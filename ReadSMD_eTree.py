import xml.etree.ElementTree as ET
import time

def xmlSMD2ListofDictionaries(filename):
    
    with open(filename,'rt') as smdfile:
        tree = ET.parse(smdfile)

    root = tree.getroot()

    table = []  # Create a list to act as a table that will contain dictionary objects as rows.

    for cat in root.iter('Category'):

        pCategory = cat.attrib.get('name')

        for pItem in cat.iter('Item'):

            rowDict = {}

            rowDict['Category'] = pCategory
            rowDict['FeatureName'] = pItem.attrib.get('featureName')
            rowDict['FeatureDescription'] = pItem.attrib.get('featureDescription')

            pPointFeature = pItem.find('PointFeature')

            rowDict['FeatureToggle'] = pPointFeature.find('PointFeatureToggle').text
            rowDict['PointType'] = pPointFeature.find('PointType').text
            rowDict['PointRotationAngle'] = pPointFeature.find('PointRotationAngle').text
    
            pPointLocator = pPointFeature.find('PointLocator')

            pLocatorSymbol = pPointLocator.find('LocatorSymbol').text

            rowDict['LocatorSymbol'] = pLocatorSymbol

            pPointLocatorSymbology = pPointLocator.find('LocatorSymbology')

            rowDict['PointLocatorSymbologyLevel'] = pPointLocatorSymbology.find('Level').text
            rowDict['PointLocatorSymbologyColor'] = pPointLocatorSymbology.find('Color').text
            rowDict['PointLocatorSymbologyWeight'] = pPointLocatorSymbology.find('Weight').text

            rowDict['PointLocatorWidth'] = pPointLocator.find('LocatorWidth').text
            rowDict['PointLocatorScale'] = pPointLocator.find('LocatorScale').text

            pPointLocatorCircleSymbology = pPointLocator.find('LocatorCircleSymbology')

            rowDict['PointLocatorCircleSymbologyLevel'] = pPointLocatorSymbology.find('Level').text
            rowDict['PointLocatorCircleSymbologyColor'] = pPointLocatorSymbology.find('Color').text
            rowDict['PointLocatorCircleSymbologyWeight'] = pPointLocatorSymbology.find('Weight').text

            rowDict['PointLocatorCircleRadius'] = pPointLocator.find('LocatorCircleRadius').text
            rowDict['PointLocatorCircleScaleOption'] = pPointLocator.find('LocatorCircleScaleOption').text
            rowDict['PointLocatorCircleScale'] = pPointLocator.find('LocatorCircleScale').text

            pPointCell = pPointFeature.find('PointCell')

            rowDict['PointCellLib'] = pPointCell.find('PointCellLib').text
            rowDict['PointCellName'] = pPointCell.find('PointCellName').text
            rowDict['PointCellRelativeOption'] = pPointCell.find('PointCellRelativeOption').text

            pPointCellSymbology = pPointCell.find('PointCellSymbology')

            rowDict['PointCellSymbologyLevel'] = pPointCellSymbology.find('Level').text
            rowDict['PointCellSymbologyColor'] = pPointCellSymbology.find('Color').text
            rowDict['PointCellSymbologyType'] = pPointCellSymbology.find('Style').attrib.get('type')
            rowDict['PointCellSymbologyStyle'] = pPointCellSymbology.find('Style').text
            rowDict['PointCellSymbologyWeight'] = pPointCellSymbology.find('Weight').text

            rowDict['PointCreationScaleUseToggle'] = pPointCell.find('PointCreationScaleUseToggle').text
            rowDict['PointCreationScale'] = pPointCell.find('PointCreationScale').text

            pPointSymbol = pPointFeature.find('PointSymbol')

            rowDict['PointCharactor'] = pPointSymbol.find('PointCharactor').text

            pPointSymbology = pPointSymbol.find('PointSymbology')

            pPointLinearSymbology = pPointSymbology.find('LinearSymbology')

            rowDict['PointLinearSymbologyLevel'] = pPointLinearSymbology.find('Level').text
            rowDict['PointLinearSymbologyColor'] = pPointLinearSymbology.find('Color').text
            rowDict['PointLinearSymbologyWeight'] = pPointLinearSymbology.find('Weight').text

            pPointSymbolTextPreference = pPointSymbology.find('TextPreference')

            rowDict['PointSymbolTextPrefHeight'] = pPointSymbolTextPreference.find('Height').text
            rowDict['PointSymbolTextPrefWidth'] = pPointSymbolTextPreference.find('Width').text
            rowDict['PointSymbolTextPrefJustificationH'] = pPointSymbolTextPreference.find('JustificationH').text
            rowDict['PointSymbolTextPrefJustificationV'] = pPointSymbolTextPreference.find('JustificationV').text
            rowDict['PointSymbolTextPrefFont_type'] = pPointSymbolTextPreference.find('Font').attrib.get('type')
            rowDict['PointSymbolTextPrefFont'] = pPointSymbolTextPreference.find('Font').text
            rowDict['PointSymbolTextPrefScaleOption'] = pPointSymbolTextPreference.find('ScaleOption').text
            rowDict['PointSymbolTextPrefScale'] = pPointSymbolTextPreference.find('Scale').text

            pPointLabelSymbology = pPointFeature.find('LabelSymbology')

            pNameLabel = pPointLabelSymbology.find('NameLabel')

            rowDict['NameLabelToggle'] = pNameLabel.find('NameLabelToggle').text

            pNameLabelSymbology = pNameLabel.find('NameLabelSymbology')

            pNameLabelLinearSymbology = pNameLabelSymbology.find('LinearSymbology')

            rowDict['NameLabelLinearSymbologyLevel'] = pNameLabelLinearSymbology.find('Level').text
            rowDict['NameLabelLinearSymbologyColor'] = pNameLabelLinearSymbology.find('Color').text
            rowDict['NameLabelLinearSymbologyWeight'] = pNameLabelLinearSymbology.find('Weight').text

            pNameLabelTextPref = pNameLabelSymbology.find('TextPreference')

            rowDict['NameLabelTextPrefHeight'] = pNameLabelTextPref.find('Height').text
            rowDict['NameLabelTextPrefWidth'] = pNameLabelTextPref.find('Width').text
            rowDict['NameLabelTextPrefJustificationH'] = pNameLabelTextPref.find('JustificationH').text
            rowDict['NameLabelTextPrefJustificationV'] = pNameLabelTextPref.find('JustificationV').text
            rowDict['NameLabelTextPrefFont_type'] = pNameLabelTextPref.find('Font').attrib.get('type')
            rowDict['NameLabelTextPrefFont'] = pNameLabelTextPref.find('Font').text
            rowDict['NameLabelTextPrefScaleOption'] = pNameLabelTextPref.find('ScaleOption').text
            rowDict['NameLabelTextPrefScale'] = pNameLabelTextPref.find('Scale').text

            pNameLabelTextFormat = pNameLabelSymbology.find('Format')

            rowDict['NameLabelFormatPrefix'] = pNameLabelTextFormat.find('Prefix').text
            rowDict['NameLabelFormatSuffix'] = pNameLabelTextFormat.find('Suffix').text

            pElevationLabel = pPointLabelSymbology.find('ElevationLabel')

            rowDict['ElevationLabelToggle'] = pElevationLabel.find('ElevationLabelToggle').text

            pElevationLabelSymbology = pElevationLabel.find('ElevationLabelSymbology')

            pElevationLabelLinearSymbology = pElevationLabelSymbology.find('LinearSymbology')

            rowDict['ElevationLabelLinearSymbologyLevel'] = pElevationLabelLinearSymbology.find('Level').text
            rowDict['ElevationLabelLinearSymbologyColor'] = pElevationLabelLinearSymbology.find('Color').text
            rowDict['ElevationLabelLinearSymbologyWeight'] = pElevationLabelLinearSymbology.find('Weight').text        

            pElevationLabelTextPref = pElevationLabelSymbology.find('TextPreference')

            rowDict['ElevationLabelTextPrefHeight'] = pElevationLabelTextPref.find('Height').text
            rowDict['ElevationLabelTextPrefWidth'] = pElevationLabelTextPref.find('Width').text
            rowDict['ElevationLabelTextPrefJustificationH'] = pElevationLabelTextPref.find('JustificationH').text
            rowDict['ElevationLabelTextPrefJustificationV'] = pElevationLabelTextPref.find('JustificationV').text
            rowDict['ElevationLabelTextPrefFont_type'] = pElevationLabelTextPref.find('Font').attrib.get('type')
            rowDict['ElevationLabelTextPrefFont'] = pElevationLabelTextPref.find('Font').text
            rowDict['ElevationLabelTextPrefScaleOption'] = pElevationLabelTextPref.find('ScaleOption').text
            rowDict['ElevationLabelTextPrefScale'] = pElevationLabelTextPref.find('Scale').text        

            pElevationLabelFormat = pElevationLabelSymbology.find('Format')

            rowDict['ElevationLabelFormatPrefix'] = pElevationLabelFormat.find('Prefix').text
            rowDict['ElevationLabelFormatSuffix'] = pElevationLabelFormat.find('Suffix').text

            pCommentLabel = pPointLabelSymbology.find('CommentLabel')

            rowDict['CommentLabelToggle'] = pCommentLabel.find('CommentLabelToggle').text

            pCommentLabel = pPointLabelSymbology.find('CommentLabel')

            pCommentLabelSymbology = pCommentLabel.find('CommentLabelSymbology')

            pCommentLabelLinearSymbology = pCommentLabelSymbology.find('LinearSymbology')

            rowDict['CommentLabelLinearSymbologyLevel'] = pCommentLabelLinearSymbology.find('Level').text
            rowDict['CommentLabelLinearSymbologyColor'] = pCommentLabelLinearSymbology.find('Color').text
            rowDict['CommentLabelLinearSymbologyWeight'] = pCommentLabelLinearSymbology.find('Weight').text        

            pCommentLabelTextPref = pCommentLabelSymbology.find('TextPreference')

            rowDict['CommentLabelTextPrefHeight'] = pCommentLabelTextPref.find('Height').text
            rowDict['CommentLabelTextPrefWidth'] = pCommentLabelTextPref.find('Width').text
            rowDict['CommentLabelTextPrefJustificationH'] = pCommentLabelTextPref.find('JustificationH').text
            rowDict['CommentLabelTextPrefJustificationV'] = pCommentLabelTextPref.find('JustificationV').text
            rowDict['CommentLabelTextPrefFont_type'] = pCommentLabelTextPref.find('Font').attrib.get('type')
            rowDict['CommentLabelTextPrefFont'] = pCommentLabelTextPref.find('Font').text
            rowDict['CommentLabelTextPrefScaleOption'] = pCommentLabelTextPref.find('ScaleOption').text
            rowDict['CommentLabelTextPrefScale'] = pCommentLabelTextPref.find('Scale').text

            pDescriptionLabel = pPointLabelSymbology.find('DescriptionLabel')

            rowDict['DescriptionLabelToggle'] = pDescriptionLabel.find('DescriptionLabelToggle').text

            pDescriptionLabel = pPointLabelSymbology.find('DescriptionLabel')

            pDescriptionLabelSymbology = pDescriptionLabel.find('DescriptionLabelSymbology')

            pDescriptionLabelLinearSymbology = pDescriptionLabelSymbology.find('LinearSymbology')

            rowDict['DescriptionLabelLinearSymbologyLevel'] = pDescriptionLabelLinearSymbology.find('Level').text
            rowDict['DescriptionLabelLinearSymbologyColor'] = pDescriptionLabelLinearSymbology.find('Color').text
            rowDict['DescriptionLabelLinearSymbologyWeight'] = pDescriptionLabelLinearSymbology.find('Weight').text        

            pDescriptionLabelTextPref = pDescriptionLabelSymbology.find('TextPreference')

            rowDict['DescriptionLabelTextPrefHeight'] = pDescriptionLabelTextPref.find('Height').text
            rowDict['DescriptionLabelTextPrefWidth'] = pDescriptionLabelTextPref.find('Width').text
            rowDict['DescriptionLabelTextPrefJustificationH'] = pDescriptionLabelTextPref.find('JustificationH').text
            rowDict['DescriptionLabelTextPrefJustificationV'] = pDescriptionLabelTextPref.find('JustificationV').text
            rowDict['DescriptionLabelTextPrefFont_type'] = pDescriptionLabelTextPref.find('Font').attrib.get('type')
            rowDict['DescriptionLabelTextPrefFont'] = pDescriptionLabelTextPref.find('Font').text
            rowDict['DescriptionLabelTextPrefScaleOption'] = pDescriptionLabelTextPref.find('ScaleOption').text
            rowDict['DescriptionLabelTextPrefScale'] = pDescriptionLabelTextPref.find('Scale').text

            pLabelPosition = pPointFeature.find('LabelPosition')

            rowDict['NamePosition'] = pLabelPosition.find('NamePosition').text
            rowDict['ElevationPosition'] = pLabelPosition.find('ElevationPosition').text
            rowDict['NumberOfCharBeforeElevationDecimal'] = pLabelPosition.find('NumberOfCharBeforeElevationDecimal').text
            rowDict['NumberOfCharAfterElevationDecimal'] = pLabelPosition.find('NumberOfCharAfterElevationDecimal').text
            rowDict['CommentPosition'] = pLabelPosition.find('CommentPosition').text
            rowDict['CommentLength'] = pLabelPosition.find('CommentLength').text
            rowDict['DescriptionPosition'] = pLabelPosition.find('DescriptionPosition').text
            rowDict['DescriptionLength'] = pLabelPosition.find('DescriptionLength').text
            rowDict['PlotRadialToggle'] = pLabelPosition.find('PlotRadialToggle').text
            rowDict['SetGraphicGroupToggle'] = pLabelPosition.find('SetGraphicGroupToggle').text
            rowDict['DistanceAwayFromOrigin'] = pLabelPosition.find('DistanceAwayFromOrigin').text

            pDescritionComposition = pPointFeature.find('DescritionComposition')

            pCurrentDescription = pDescritionComposition.find('CurrentDescription')

            rowDict['CurrentDescriptiveName'] = pCurrentDescription.find('CurrentDescriptiveName').text
            rowDict['CurrentDescriptivePrefix'] = pCurrentDescription.find('CurrentDescriptivePrefix').text
            rowDict['CurrentDescriptiveSuffix'] = pCurrentDescription.find('CurrentDescriptiveSuffix').text

            pDescriptionList = pDescritionComposition.find('DescriptionList')

            pDescription = pDescriptionList.find('Description')

            if pDescriptionList.find('Description') is None:
                rowDict['DescriptiveName'] = "DOES NOT EXISTS"
                rowDict['DescriptivePrefix'] = "DOES NOT EXISTS"
                rowDict['DescriptiveSuffix'] = "DOES NOT EXISTS"
            else:
                rowDict['DescriptiveName'] = pDescription.find('DescriptiveName').text
                rowDict['DescriptivePrefix'] = pDescription.find('DescriptivePrefix').text
                rowDict['DescriptiveSuffix'] = pDescription.find('DescriptiveSuffix').text        

            rowDict['DesriptionFirst'] = pDescritionComposition.find('DesriptionFirst').text
            rowDict['TotalDescription'] = pDescritionComposition.find('TotalDescription').text

            pDescriptionParameter = pPointFeature.find('DescriptionParameter')

            rowDict['DescriptionParameterToggle'] = pDescriptionParameter.find('DescriptionParameterToggle').text

            pCurrentParameter = pDescriptionParameter.find('CurrentParameter')

            rowDict['CurrentFieldName'] = pCurrentParameter.find('CurrentFieldName').text
            rowDict['CurrentAlias'] = pCurrentParameter.find('CurrentAlias').text
            rowDict['CurrentDataType'] = pCurrentParameter.find('CurrentDataType').text

            rowDict['ParameterList'] = pDescriptionParameter.find('ParameterList').text
            rowDict['ParameterFirst'] = pDescriptionParameter.find('ParameterFirst').text
            rowDict['TotalParameter'] = pDescriptionParameter.find('TotalParameter').text       

            pAdjustSize = pPointFeature.find('AdjustSize')

            rowDict['AdjustSizeToggle'] = pAdjustSize.find('AdjustSizeToggle').text
            rowDict['XScale'] = pAdjustSize.find('XScale').text
            rowDict['YScale'] = pAdjustSize.find('YScale').text
            rowDict['ZScale'] = pAdjustSize.find('ZScale').text
            rowDict['ApplyPlotScaleToggle'] = pAdjustSize.find('ApplyPlotScaleToggle').text

            pLinearFeature = pItem.find('LinearFeature')

            rowDict['LinearFeatureToggle'] = pLinearFeature.find('LinearFeatureToggle').text

            pLinearFeatureSymbology = pLinearFeature.find('LinearFeatureSymbology')

            rowDict['LinearFeatureSymbologyLevel'] = pLinearFeatureSymbology.find('Level').text
            rowDict['LinearFeatureSymbologyColor'] = pLinearFeatureSymbology.find('Color').text
            rowDict['LinearFeatureSymbologyStyle_type'] = pLinearFeatureSymbology.find('Style').attrib.get('type')
            rowDict['LinearFeatureSymbologyStyle'] = pLinearFeatureSymbology.find('Style').text
            rowDict['LinearFeatureSymbologyWeight'] = pLinearFeatureSymbology.find('Weight').text

            rowDict['LinearScaleOption'] = pLinearFeature.find('LinearScaleOption').text
            rowDict['LinearScale'] = pLinearFeature.find('LinearScale').text

            pLinkingCode = pItem.find('LinkingCode')

            rowDict['LinkingCodeToggle'] = pLinkingCode.find('LinkingCodeToggle').text
            rowDict['LinkingCodel'] = pLinkingCode.find('LinkingCodel').text        

            pDTMControl = pItem.find('DTMControl')

            rowDict['DTMControl'] = pDTMControl.find('DTMControl').text
            rowDict['ZoneControl'] = pDTMControl.find('ZoneControl').text

            table.append(rowDict)

    return table