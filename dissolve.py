# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# dissolve.py
# Created on: 2016-04-26 12:03:19.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: dissolve <input_data>
# Description:
# ---------------------------------------------------------------------------
#run this first no args
#C:\Python27\ArcGIS10.3\python.exe dissolve.py
# Import arcpy module
import arcpy
import json
import os


# Script arguments
input_data = arcpy.GetParameterAsText(0)

# Local variables:

#input data
path = "E:\\ncdeq\\DMS_RBRP.gdb"
temp_dissolve = "E:\\DMS_RBRP.gdb\\temp_dissolve"


#output data
outPathGDB = "E:\\ncdeq\\code\\ncdeq-data"
outGDB = "RDRBP_AGO.gdb"

#baseLine data
with open('json/baseline_mapping.json') as data_file:
    BaseLineData = json.load(data_file)

#uplift data
with open('json/uplift_mapping.json') as data_file:
    uplift_Data = json.load(data_file)

#transposed_template data
with open('json/transposed_template.json') as data_file:
    transposedTemplate = json.load(data_file)


outGDBFull =  os.path.join(outPathGDB, outGDB)

#if the ncdeq_normailized data exists delete and so we can create a new version
if arcpy.Exists(outGDBFull):
	arcpy.Delete_management(outGDBFull)

#create a new ncdeq_normailized geodatabase
arcpy.CreateFileGDB_management (outPathGDB, outGDB, "10.0")

#result data
transposed =  os.path.join(outGDBFull, 'ncdeq_normailized')

#create a new normalized table
arcpy.CreateTable_management(outGDBFull,'ncdeq_normailized')

#create the new fiels from the template
for field in transposedTemplate:
	fieldName = field['fieldname']
	fieldType = field['fieldType']
	fieldLength = field['Length']
	arcpy.AddField_management(transposed, fieldName, fieldType, "", "", fieldLength, "", "NULLABLE", "NON_REQUIRED", "")

#add name fields for dissovled huc data where do I get that
#update the ago db. later

#check if field exists
def FieldExist(featureclass, fieldname):
	fieldList = arcpy.ListFields(featureclass, fieldname)

	fieldCount = len(fieldList)

	if (fieldCount == 1):
		return True
	else:
		return False

#transposed_template data
with open('json/geography_levels.json') as data_file:
    geographyLevels = json.load(data_file)

#need to add this to geography_levels.json to include catchments.
#    {'level':'Catchment','fieldName':'GRIDCODE','match':'FIRST_HUC_12','geographyLevel':4}]

aggreatate_type = "SUM"
area_AreaSqKM = 'AreaSqKM'
area_AreaShape = 'Shape_Area'

#this needs to live in code because the json data is inserted
chartTypes = [{'name':'baseline',
			   'table':'NHDCat_comb_baseline',
			   'fields_conversion':BaseLineData,
			   'fields_dissovled': [['HUC_12','FIRST'],
                                    ['AreaSqKM', aggreatate_type],
                                    ['Shape_Area', aggreatate_type],
			   						['ALL_base', aggreatate_type],
			   						['Hab_base_norm',aggreatate_type],
			   						['Hydro_base_norm', aggreatate_type],
			   						['WQ_base_norm', aggreatate_type],
									['MeanLikelihood_norm',aggreatate_type],
									['q2yr_base_norm',aggreatate_type],
									['q10yr_base_norm',aggreatate_type],
									['q50yr_base_norm',aggreatate_type],
									['q100yr_base_norm',aggreatate_type],
									['N_total_base_norm',aggreatate_type],
									['P_total_base_norm',aggreatate_type],
									['N_AG_base_norm',aggreatate_type],
									['N_URBAN_base_norm',aggreatate_type],
									['N_CMAQ2002KG_base_norm',aggreatate_type],
									['P_AG_base_norm',aggreatate_type],
									['P_URBAN_base_norm',aggreatate_type]
								   ],
			   'fields_calc': [['ALL_base', area_AreaSqKM],
			   						['Hab_base_norm',area_AreaShape],
			   						['Hydro_base_norm', area_AreaSqKM],
			   						['WQ_base_norm', area_AreaSqKM],
									['MeanLikelihood_norm',area_AreaShape],
									['q2yr_base_norm',area_AreaSqKM],
									['q10yr_base_norm',area_AreaSqKM],
									['q50yr_base_norm',area_AreaSqKM],
									['q100yr_base_norm',area_AreaSqKM],
									['N_total_base_norm',area_AreaSqKM],
									['P_total_base_norm',area_AreaSqKM],
									['N_AG_base_norm',area_AreaSqKM],
									['N_URBAN_base_norm',area_AreaSqKM],
									['N_CMAQ2002KG_base_norm',area_AreaSqKM],
									['P_AG_base_norm',area_AreaSqKM],
									['P_URBAN_base_norm',area_AreaSqKM]
								   ]},
				{'name':'uplift',
			   'table':'NHDCat_comb_uplift',
			   'fields_conversion':uplift_Data,
			   'fields_dissovled': [['HUC_12','FIRST'],
                                    ['AreaSqKM', aggreatate_type],
                                    ['Shape_Area', aggreatate_type],
			   						['ALL_uplift', aggreatate_type],
			   						['Hab_uplift_WetlandsBMPs', aggreatate_type],
			   						['Hab_uplift_AdvConv',aggreatate_type],
			   						['Hab_uplift_AqCon', aggreatate_type],
			   						['Hab_uplift_Restoration',aggreatate_type],
			   						['Hab_uplift_norm',aggreatate_type],
									['Hydro_uplift_norm', aggreatate_type],
									['WQ_uplift_norm', aggreatate_type],
									['MeanLikelihood_norm',aggreatate_type],
									['q2yr_uplift_norm',aggreatate_type],
									['q10yr_uplift_norm',aggreatate_type],
									['q50yr_uplift_norm',aggreatate_type],
									['q100yr_uplift_norm',aggreatate_type],
									['N_total_uplift_norm',aggreatate_type],
									['P_total_uplift_norm',aggreatate_type],
									['N_AG_uplift_norm',aggreatate_type],
									['N_URBAN_uplift_norm',aggreatate_type],
									['N_CMAQ2002KG_uplift_norm',aggreatate_type],
									['P_AG_uplift_norm',aggreatate_type],
									['P_URBAN_uplift_norm',aggreatate_type]
								   ],
		   'fields_calc': [['ALL_uplift', area_AreaSqKM],
                                ['Hab_uplift_WetlandsBMPs', area_AreaShape],
                                ['Hab_uplift_AdvConv',area_AreaShape],
                                ['Hab_uplift_AqCon', area_AreaShape],
                                ['Hab_uplift_Restoration',area_AreaShape],
                                ['Hab_uplift_norm',area_AreaShape],
                                ['Hydro_uplift_norm', area_AreaSqKM],
                                ['WQ_uplift_norm', area_AreaSqKM],
                                ['MeanLikelihood_norm',area_AreaShape],
                                ['q2yr_uplift_norm',area_AreaSqKM],
                                ['q10yr_uplift_norm',area_AreaSqKM],
                                ['q50yr_uplift_norm',area_AreaSqKM],
                                ['q100yr_uplift_norm',area_AreaSqKM],
                                ['N_total_uplift_norm',area_AreaSqKM],
                                ['P_total_uplift_norm',area_AreaSqKM],
                                ['N_AG_uplift_norm',area_AreaSqKM],
                                ['N_URBAN_uplift_norm',area_AreaSqKM],
                                ['N_CMAQ2002KG_uplift_norm',area_AreaSqKM],
                                ['P_AG_uplift_norm',area_AreaSqKM],
                                ['P_URBAN_uplift_norm',area_AreaSqKM]
                               ]}]

#empty table of exists
if arcpy.Exists(transposed):
	arcpy.DeleteRows_management(transposed)

for chartType in chartTypes:
	print 'Chart Type: ' + chartType['name']
	chartTypeName = chartType['name']

    #source feature layer
	inputFC =  os.path.join(path, chartType['table'])

	#get fields in input data
	fields = arcpy.ListFields(  os.path.join(path, inputFC)  )

	#get json data for how to deal with each field
	input_dict = chartType['fields_conversion']

	#if feature class exists delete
	if arcpy.Exists(temp_dissolve):
		arcpy.Delete_management(temp_dissolve)


	for geog in geographyLevels:
		currentGeographyLevel = geog['fieldName']
		print 'Dissolve: ' + currentGeographyLevel
		print '  ' + geog['level']

        #setup temp dissolve table, one dissovled table for each field
        #   this creates one record/row for each topic or chart type
		temp_dissolve = os.path.join(outGDBFull, geog['level'])
	 	dissolve = os.path.join(outGDBFull, 'dissolve')

		#temp feature layer to calcualted weighted area averages
		temp_inputFC =  os.path.join(path, chartType['table'] + '_temp')

		#if feature class exists delete
		if arcpy.Exists(temp_dissolve):
			arcpy.Delete_management(temp_dissolve)

		#dissolve on geographyLevels
		StatisticsFields = chartType['fields_dissovled']

		#temp feature layer to calcualted weighted area averages
		temp_inputFC =  os.path.join(path, chartType['table'] + '_temp')

		#if feature class exists delete
		if arcpy.Exists(temp_inputFC):
			arcpy.Delete_management(temp_inputFC)

		#copy features from existing table to temp table we will delete it later
		arcpy.CopyFeatures_management(inputFC, temp_inputFC)

		#check of huc 6 exists if not add and calculae field
		# or is it better to not mutate the data and create a copy... and delete copy after processings
		if not FieldExist(temp_inputFC,'HUC_6'):
			#add field
			arcpy.AddField_management(temp_inputFC, "HUC_6", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
			#calc HUC_6
			arcpy.CalculateField_management(temp_inputFC, "HUC_6", "!HUC_12![0:6]", "PYTHON", "")

		#dissolve on geographyLevels
		Calc_Fields = chartType['fields_calc']

        # #attempt at weighted aveage first part calulate score * area
        # formulate is sum if all (value*area) / sum of all areas 
		for fld in Calc_Fields:
			arcpy.CalculateField_management(temp_inputFC, fld[0], "!" +  fld[0] + "! * !" +  fld[1] + "!", "PYTHON", "")

        #dissolve based on geography level (huc12,huc8,huc6)
		arcpy.Dissolve_management(temp_inputFC, temp_dissolve, currentGeographyLevel, StatisticsFields, "MULTI_PART", "DISSOLVE_LINES" )

        #attempt at weighted avg second part dissolve and calulate the sum of all the weghted scores (area*score) dived by the sum of areas
		for fld in Calc_Fields:
			arcpy.CalculateField_management(temp_dissolve,  aggreatate_type + "_" + fld[0], "!" + aggreatate_type + "_" + fld[0] + "!/!" + aggreatate_type + "_" +  fld[1] + "!", "PYTHON", "")

		#iterate fields and to send dissolve
		for field in fields:

			#find matching instance of field on data.
			#then use this to construct the dissilove varriables.
			output_dict = [x for x in input_dict if x['fieldName'] == field.name]

			#if field exists in template we will use the field in output ddata.
			#  need to know who we want the table data formated - derieved from tempatle json
			if (output_dict):
				transposeField = output_dict[0]['fieldName']
				temp_transposed = os.path.join(outGDB, 'temp_transposed_' + currentGeographyLevel + '_'  + transposeField)
				# temp_transposed = os.path.join(outGDB,'test')

				#if feature class exists delete
				if arcpy.Exists(temp_transposed):
					arcpy.Delete_management(temp_transposed)

                #normalized data as in database normalization
				arcpy.TransposeFields_management(temp_dissolve, aggreatate_type + "_" + transposeField + " " + aggreatate_type + "_" + transposeField, temp_transposed, "chart_label", "chart_value", currentGeographyLevel + ";FIRST_HUC_12")

				print '  ' + transposeField
				for f in output_dict[0]:
					print '    ' + f

                #add fields from template to the normalized table if they do not exist
				for field in transposedTemplate:
					fieldName = field['fieldname']
					fieldType = field['fieldType']
					fieldLength = field['Length']
					if not FieldExist(temp_transposed,fieldName):
						arcpy.AddField_management(temp_transposed, fieldName, fieldType, "", "", fieldLength, "", "NULLABLE", "NON_REQUIRED", "")

				# Process: calculate_geography_level
				arcpy.CalculateField_management(temp_transposed, "geography_level",   geog['geographyLevel'], "PYTHON", "")

				# Process: calculate_geography_match_id
				if  geog['level'] == 'Catchment':
					arcpy.CalculateField_management(temp_transposed, "geography_match_id",  "!"+ geog['match']+"!", "PYTHON", "")
				else:
					arcpy.CalculateField_management(temp_transposed, "geography_match_id", "!"+currentGeographyLevel+"![0:"+ geog['match']+"]", "PYTHON", "")

				#process: chart Description
				arcpy.CalculateField_management(temp_transposed, "chart_description", "'" + output_dict[0]['chartDescription'] + "'", "PYTHON", "")

				# Process: Calculate_chart_type
				arcpy.CalculateField_management(temp_transposed, "chart_id","'" + output_dict[0]['chartId'] + "'" , "PYTHON", "")

				# Process: Calculate_chart_type
				arcpy.CalculateField_management(temp_transposed, "chart_matchid","'" + output_dict[0]['chartMatchId'] + "'" , "PYTHON", "")

				# Process: Calculate_chart_type
				arcpy.CalculateField_management(temp_transposed, "chart_type","'" + output_dict[0]['chartType'] + "'" , "PYTHON", "")

				# Process: Calculate_chart_level_label
				arcpy.CalculateField_management(temp_transposed, "chart_level_label", "'" + output_dict[0]['chartLabel'] + "'", "PYTHON", "")

				# Process: Calculate_chart_level
				arcpy.CalculateField_management(temp_transposed, "chart_level", "'" + output_dict[0]['chartLevel'] + "'", "PYTHON", "")

				arcpy.CalculateField_management(temp_transposed, "id", "!" + geog['fieldName'] + "!" , "PYTHON", "")

				# Process: Calculate_id
				arcpy.CalculateField_management(temp_transposed, "geography_label", "'"+ geog['level']+"'", "PYTHON", "")

				#round to two decimealss
				arcpy.CalculateField_management(temp_transposed, "chart_value", "round(float(!chart_value!),8)", "PYTHON", "")

				if FieldExist(temp_inputFC,currentGeographyLevel):
					deleteFields = []
					deleteFields.append(currentGeographyLevel)
					t = arcpy.DeleteField_management(temp_transposed, deleteFields)

				#remove huc12
				if FieldExist(temp_transposed,'FIRST_HUC_12'):
					deleteFields = []
					deleteFields.append('FIRST_HUC_12')
					t = arcpy.DeleteField_management(temp_transposed, deleteFields)

				if FieldExist(temp_dissolve, aggreatate_type + "_" + transposeField):
					deleteFields =[]
					deleteFields.append( aggreatate_type + "_" + transposeField)
					arcpy.DeleteField_management(temp_dissolve, deleteFields)

				#append to transpose
				arcpy.Append_management(temp_transposed,transposed)

				#delete temp transpose
				if arcpy.Exists(temp_transposed):
					arcpy.Delete_management(temp_transposed)


for geog in geographyLevels:
	temp_dissolve = os.path.join(outGDBFull, geog['level'])

	if FieldExist(temp_dissolve, geog['fieldName']):
		arcpy.AlterField_management(temp_dissolve,  geog['fieldName'], "id", "id", "", "", "NON_NULLABLE", "false")

	if FieldExist(temp_dissolve, 'FIRST_HUC_12'):
		deleteFields =[]
		deleteFields.append('FIRST_HUC_12')
		arcpy.DeleteField_management(temp_dissolve, deleteFields)


for chartType in chartTypes:
	print 'Chart Type: ' + chartType['name']
	chartTypeName = chartType['name']

    #temp feature layer to calcualted weighted area averages
	temp_inputFC =  os.path.join(path, chartType['table'] + '_temp')

    #if huc_6 exists delete it
	if FieldExist(temp_inputFC,'HUC_6'):
		deleteFields = []
		deleteFields.append('HUC_6')
		t = arcpy.DeleteField_management(temp_inputFC, deleteFields)

	#if feature class exists delete
	if arcpy.Exists(temp_inputFC):
		arcpy.Delete_management(temp_inputFC)
