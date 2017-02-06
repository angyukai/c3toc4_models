
# coding: utf-8

# ### Preparing data with index

# In[ ]:

import pandas as pd
import plotly.plotly as py
from plotly import tools
import plotly.graph_objs as go

#for plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

def totalAbsFlux(sol_M1M2):
    totalFlux = 0
    
    for i in sol_M1M2:
        totalFlux += sol_M1M2[i]
        
    return totalFlux

#TO BE DELETED
# def RubiscoEfficiencyAnalysis(solM,m1m2,totalSteps = 20,maxRatio = 10.0, carbox = 1, oxy = 1, filename = None):
    
#     step = maxRatio/totalSteps
#     step = round(step,2)
#     m1m2_photon = []
#     m_photon = solM['Photon_Light_tx']
#     ratio_index = []
    
#     for i in range(totalSteps):
        
#         try:
#             m1m2.DelMetabolite('RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2_RXN-961_Light_p_M2_fixedratio')
#             m1m2.SetReacsFixedRatio({"RXN-961_Light_p_M2":oxy, "RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2":carbox})
#             m1m2.MinFluxSolve()
#         except ValueError:
#             m1m2.DelMetabolite('RXN-961_Light_p_M2_RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2_fixedratio')
#             m1m2.SetReacsFixedRatio({"RXN-961_Light_p_M2":oxy, "RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2":carbox})
#             m1m2.MinFluxSolve()
            
#         print 'carbox:oxy |', carbox,':',oxy 
        
#         solM1M2 = m1m2.GetSol()

#         photonDiff = solM1M2['Photon_Light_tx_M1'] + solM1M2['Photon_Light_tx_M2'] - solM['Photon_Light_tx']
        
#         print 'M1M2-M photon diff: ', photonDiff
#         if (photonDiff) < 0:
#             print 'EFFICIENCY THRESHOLD: carbox:oxy | ', carbox,':',oxy
        
#         #preparing lists for dataframe
#         m1m2_photon.append(solM1M2['Photon_Light_tx_M1'] + solM1M2['Photon_Light_tx_M2'])
#         ratio_index.append(str(carbox)+':'+str(oxy))
        
#         carbox += step

#     tempdf = pd.DataFrame({'M1M2_Photon':m1m2_photon,'M_photon':m_photon},index = ratio_index)
#     tempGroup = [tempdf,'Photonstuff']
    
#     print tempGroup[1]
#     print tempGroup[0]
    
#     M1M2_photon = go.Bar(
#             x= ratio_index,
#             y= m1m2_photon,
#             name = 'photons'
#         )
    
    
#     data = [M1M2_photon]
    
#     layout = {
        
#         'shapes': [
#             {'type': 'line',
#                 'x0': -1,
#                 'y0': m_photon,
#                 'x1': len(m1m2_photon),
#                 'y1': m_photon,
#                 'line': {
#                     'color': 'rgb(255, 0, 0)',
#                     'width': 2,
#                     'dash': 'dashdot',
#                 },
#             }
#         ]
#     }

    
#     fig = {
#         'data': data,
#         'layout': layout,
#     }
    

#     iplot(fig, filename = 'photon-testing-plot')


#     if filename!= None :

#         # Create a Pandas Excel writer using XlsxWriter as the engine.
#         writer = pd.ExcelWriter(filename, engine='xlsxwriter')
#         tempdf.to_excel(writer, sheet_name='Sheet1',startcol = 1)
#         # Close the Pandas Excel writer and output the Excel file.
#         writer.save()
        
def RubiscoEfficiencyAnalysis(solM,m1m2,totalSteps = 20,maxRatio = 10.0, carbox = 1, oxy = 1, filename = None, mainTitle = 'Default Title'):
    
    step = maxRatio/totalSteps
    step = round(step,2)
    m1m2_photon = []
    m_photon = solM['Photon_Light_tx']
    ratio_index = []
    
    for i in range(totalSteps):
        
        try:
            m1m2.DelMetabolite('RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2_RXN-961_Light_p_M2_fixedratio')
            m1m2.SetReacsFixedRatio({"RXN-961_Light_p_M2":oxy, "RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2":carbox})
            m1m2.MinFluxSolve()
        except ValueError:
            m1m2.DelMetabolite('RXN-961_Light_p_M2_RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2_fixedratio')
            m1m2.SetReacsFixedRatio({"RXN-961_Light_p_M2":oxy, "RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p_M2":carbox})
            m1m2.MinFluxSolve()
            
        print 'carbox:oxy |', carbox,':',oxy 
        
        solM1M2 = m1m2.GetSol()

        photonDiff = solM1M2['Photon_Light_tx_M1'] + solM1M2['Photon_Light_tx_M2'] - solM['Photon_Light_tx']
        
        print 'M1M2-M photon diff: ', photonDiff
        if (photonDiff) < 0:
            print 'EFFICIENCY THRESHOLD: carbox:oxy | ', carbox,':',oxy
        
        #preparing lists for dataframe
        m1m2_photon.append(solM1M2['Photon_Light_tx_M1'] + solM1M2['Photon_Light_tx_M2'])
        ratio_index.append(str(carbox)+':'+str(oxy))
        
        carbox += step

    tempdf = pd.DataFrame({'Ratios':ratio_index,'M1M2_Photon':m1m2_photon,'M_photon':m_photon},index=ratio_index)
    tempGroup = [tempdf,'Photonstuff']
    
    print tempGroup[1]
    print tempGroup[0]
    

    rxn = tempdf.index
    photon = tempdf['M1M2_Photon']
    
    df = pd.DataFrame({'x':rxn,'y':photon})
    
    photon_data1 = go.Bar(
            x=df['x'],
            y=df['y'],
            name = 'M1'
        )

    trace1 = go.Scatter(
        x=0,
        y=1,
        mode='lines+markers+text',
        name='Lines, Markers and Text',
        text=['Efficiency Threshold'],
        textposition='top'
    )

    layout = go.Layout(
        
        yaxis=dict(
        title='Photon Flux',
        ),
        
        xaxis=dict(
        title='Carboxylase : Oxygenase (Ratio)',
        ),
        
        shapes= [
            {'type': 'line',
                'x0': -1,
                'y0': m_photon,
                'x1': len(m1m2_photon),
                'y1': m_photon,
                'line': {
                    'color': 'rgb(255, 0, 0)',
                    'width': 2,
                    'dash': 'dashdot',
                },
            }
        ]

    )
    
    data = [photon_data1,trace1]
    fig = go.Figure(data=data, layout=layout)
    fig['layout'].update(title=mainTitle)
    iplot(fig)
    
    if filename!= None :

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        tempdf.to_excel(writer, sheet_name='Sheet1',startcol = 1)
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()


        

def prepareDataWithCustomIndex(sol_M1M2, sol_M, reacList, customIndex, M1M2only = False):

    all_M_rxn = []
    all_M1_rxn = []
    all_M2_rxn = []
    all_index = []
    all_M1M2_rxn = []
    
    if M1M2only:
        
        for rxn in range(len(reacList)):

            lightRxn = reacList[rxn][0]
            darkRxn = reacList[rxn][1]
            tempM1M2 = [sol_M1M2[lightRxn],sol_M1M2[darkRxn]]

            tempIndex = customIndex[rxn]

            for rxn in tempM1M2:
                all_M1M2_rxn.append(rxn)
            for i in tempIndex:
                all_index.append(i)

        return all_M1M2_rxn, all_index
    
    
    else:

        for rxn in range(len(reacList)):

            lightRxn = reacList[rxn][0]
            darkRxn = reacList[rxn][1]
            tempM1 = [sol_M1M2[lightRxn+'_M1'],sol_M1M2[darkRxn+'_M1']]
            tempM2 = [sol_M1M2[lightRxn+'_M2'],sol_M1M2[darkRxn+'_M2']]
            try:
                tempM = [sol_M[lightRxn],sol_M[darkRxn]]
            except KeyError:
                tempM = [0.0,0.0]
            tempIndex = customIndex[rxn]

            for rxn in tempM1:
                all_M1_rxn.append(rxn)
            for rxn in tempM2:
                all_M2_rxn.append(rxn)
            for rxn in tempM:
                all_M_rxn.append(rxn)
            for i in tempIndex:
                all_index.append(i)

        return all_M1_rxn, all_M2_rxn, all_M_rxn, all_index


# ### Function for visualising reactions in categories, and writing to excel sheet

# In[ ]:

def visualizeDataCategories(sol_M1M2, sol_M, reacList = None , printData=True, writeData=False, aaConsolidate=True):

    #1. C3 to C4 reaction steps
    #2. Glycolysis
    #3. TCA
    #4. PPP
    #5. ETC
    #6. M1 to M2

    groupings = ['C3 to C4 Reaction Steps','Glycolysis','TCA','PPP','ETC','M1 to M2']

    print_groups = []
    excel_groups =[]
    
    #######################
    #### IMPT Reactions ###
    #######################


    rxnIndex = [
                ['Photon_Light_tx','Photon_Dark_tx'],
                ['Suc_Lt_biomass','Suc_Dk_biomass'],
                ['CO2_Lt_tx','CO2_Dk_tx'],
                ['O2_Lt_tx','O2_Dk_tx']
               ]


    reactions = [
                ['Photon_Light_tx','Photon_Dark_tx'],
                ['Sucrose_Light_biomass','Sucrose_Dark_biomass'],
                ['CO2_Light_tx','CO2_Dark_tx'],
                ['O2_Light_tx','O2_Dark_tx']
               ]
                
    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M,reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'Input/output reactions']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)
    
    #########################
    #### EVOLUTIONARY RXN ###
    #########################

    rxnIndex = [
                ['PEPCase_Lt_c','PEPCase_Dk_c'],
                ['PPDK_Lt_p','PPDK_Dk_p'],
                ['PPDK_Lt_c','PPDK_Dk_c'],
                ['CA_Lt_c','CA_Dk_c'],
                ['GLY-DC_Lt_m','GLY-DC_Dk_m'],
                #['OAA_Lt_mc','OAA_Dk_mc'],
                ['NADP-OAA-to-MAL_Lt_p','NADP-OAA-to-MAL_Dk_p'],
                ['NAD-OAA-to-MAL_Lt_p','NAD-OAA-to-MAL_Dk_p'],
                ['NAD-OAA-to-MAL_Lt_c','NAD-OAA-to-MAL_Dk_c'],
                ['ASP-AT_Lt_p','ASP-AT_Dk_p'],
                ['ASP-AT_Lt_c','ASP-AT_Dk_c'],
                ['NADP-ME_Lt_p', 'NADP-ME_Dk_p'],
                ['NADP-ME_Lt_c','NADP-ME_Dk_c'],
                ['Rubisco-Carbox_Lt_p','Rubisco-Carbox_Dk_p'],
                ['Rubisco-Oxy_Lt_p','Rubisco-Oxy_Dk_p']

               ]

    reactions = [
        
                ['PEPCARBOX-RXN_Light_c','PEPCARBOX-RXN_Dark_c'],
                ['PYRUVATEORTHOPHOSPHATE-DIKINASE-RXN_Light_p','PYRUVATEORTHOPHOSPHATE-DIKINASE-RXN_Dark_p'],
                ['PYRUVATEORTHOPHOSPHATE-DIKINASE-RXN_Light_c','PYRUVATEORTHOPHOSPHATE-DIKINASE-RXN_Dark_c'],
                ['RXN0-5224_Light_c','RXN0-5224_Dark_c'],
                ['GCVMULTI-RXN_Light_m','GCVMULTI-RXN_Dark_m'],
                 #['OAA_Pi_Light_mc','OAA_Pi_Dark_mc'],
                ['MALATE-DEHYDROGENASE-NADP+-RXN_Light_p','MALATE-DEHYDROGENASE-NADP+-RXN_Dark_p'],
                ['MALATE-DEH-RXN_Light_p','MALATE-DEH-RXN_Dark_p'],
                ['MALATE-DEH-RXN_Light_c','MALATE-DEH-RXN_Dark_c'],
                ['ASPAMINOTRANS-RXN_Light_p','ASPAMINOTRANS-RXN_Dark_p'],
                ['ASPAMINOTRANS-RXN_Light_c','ASPAMINOTRANS-RXN_Dark_c'],
                ['MALIC-NADP-RXN_Light_p','MALIC-NADP-RXN_Dark_p'],
                ['MALIC-NADP-RXN_Light_c','MALIC-NADP-RXN_Dark_c'],
                ['RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Light_p','RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_Dark_p'],
                ['RXN-961_Light_p','RXN-961_Dark_p']
        ]


    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M, reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'EVOLUTIONARY RXN']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)
    
    
    ###########################
    #### IMPT TRANSPORT RXN ###
    ###########################


    #QUESTION, ALL SHOULD BE IN THE _c?
    #Confusion on GAP vs G3p. rxn GAPXNPHOSPHN - why does GAP straight away go to DPG? and what is DPG
    rxnIndex = [
            #['GLY-DC_Lt_m','GLY-DC_Dk_m'],
                ['PEP_p_to_c_Lt','PEP_p_to_c_Dk'],
                ['OAA_MAL_Lt_pc','OAA_MAL_Dk_pc'],
                ['DHAP_3PGA_Lt_pc','DHAP_3PGA_Dk_pc']
                #['CA_Lt_c','CA_Dk_c'],
                #['OAA_Lt_mc','OAA_Dk_mc'],


               ]

    reactions = [
        #['GCVMULTI-RXN_Light_m','GCVMULTI-RXN_Dark_m'],
                ['PEP_Pi_Light_pc','PEP_Pi_Dark_pc'],
                ['OAA_MAL_Light_pc','OAA_MAL_Dark_pc'],
                ['DHAP_3PGA_Light_pc','DHAP_3PGA_Dark_pc']
                 #['RXN0-5224_Light_c','RXN0-5224_Dark_c'],
                 #['OAA_Pi_Light_mc','OAA_Pi_Dark_mc'],

        ]


    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M, reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'Transport Rxn']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)
    
    
    ############################
    #### IMPT M1M2 TRANSPORT ###
    ############################


    rxnIndex = [
        ['Malate_Lt_M1M2','Malate_Dk_M1M2'],
        ['Pyruvate_Lt_M1M2','Pyruvate_Dk_M1M2'],
        ['DHAP_Lt_M1M2','DHAP_Dk_M1M2'],
        ['G3P_Lt_M1M2','G3p_Dk_M1M2'],
        ['Sucrose_Light_M1M2','Sucrose_Dark_M1M2'],
        ['GLY_Light_M1M2','GLY_Dark_M1M2'],
        ['CO2_Light_M1M2','CO2_Dark_M1M2']
        ]

    reactions = [
        ['MAL_Light_M1M2','MAL_Dark_M1M2'],
        ['PYRUVATE_Light_M1M2','PYRUVATE_Dark_M1M2'],
        ['DIHYDROXY-ACETONE-PHOSPHATE_Light_M1M2','DIHYDROXY-ACETONE-PHOSPHATE_Dark_M1M2'],
        ['G3P_Light_M1M2','G3P_Dark_M1M2'],
        ['Sucrose_Light_M1M2','Sucrose_Dark_M1M2'],
        ['GLY_Light_M1M2','GLY_Dark_M1M2'],
        ['CO2_Light_M1M2','CO2_Dark_M1M2']

               ]


    M1M2_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M, reactions, rxnIndex, M1M2only=True)
    tempDataframe = pd.DataFrame({'M1M2':M1M2_rxn},index = indexes)
    tempGroup = [tempDataframe,'M1M2']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)
    

    ###################
    #### GLYCOLYSIS ###
    ###################

#     1. GAPDH
#     2. Hexokinase
#     3. Phosphoglucose isomerase
#     4. Phosphofructokinase
#     5. Aldolase
#     6. Triose phosphate isomerase
#     7. Phosphoglycerate kinase
#     8. Phosphoglycerate mutase
#     9. Phosphoglycerate hydratase


    #QUESTION, ALL SHOULD BE IN THE _c?
    #Confusion on GAP vs G3p. rxn GAPXNPHOSPHN - why does GAP straight away go to DPG? and what is DPG
    rxnIndex = [['Hexokinase_Lt_c ','Hexokinase_Dk_c'],
                ['Hexokinase_Lt_p','Hexokinase_Dk_p'],
                ['Hexose_P_Isomerase_Lt_c','Hexose_P_Isomerase_Dk_c'],
                ['Hexose_P_Isomerase_Lt_p','Hexose_P_Isomerase_Dk_p'],
                ['PFK_Lt_c','PFK_Dk_c'],
                ['PFK_Lt_p','PFK_Dk_p'],
                ['F16_Aldolase_Lt_c','F16_Aldolase_Dk_c'],
                ['F16_Aldolase_Lt_p','F16_Aldolase_Dk_p'],
                ['Triose_P_Isomerase_Lt_c','Triose_P_Isomerase_Dk_c'],
                ['Triose_P_Isomerase_Lt_p','Triose_P_Isomerase_Dk_p'],
                ['GAPDH_Lt_c','GAPDH_Dk_c'],
                ['GAPDH_Lt_p','GAPDH_Dk_p'],
                #reflect GAP to G3P pathway
                ['PG_Kinase_Lt_c','PG_Kinase_Dk_c'],
                ['PG_Kinase_Lt_p','PG_Kinase_Dk_p'],
                ['PG_Mutase_Lt_c','PG_Mutase_Dk_c'],
                ['PG_Mutase_Lt_p','PG_Mutase_Dk_p'],
                ['Enolase_Lt_c','Enolase_Dk_c'],
                ['Enolase_Lt_p','Enolase_Dk_p'],
                ['Pyruvate_Kinase_Lt_c','Pyruvate_Kinase_Dk_c'],
                ['Pyruvate_Kinase_Lt_p','Pyruvate_Kinase_Dk_p']

               ]

    reactions = [['GLUCOKIN-RXN_Light_c','GLUCOKIN-RXN_Dark_c'],
                 ['GLUCOKIN-RXN_Light_p','GLUCOKIN-RXN_Dark_p'],
                 ['PGLUCISOM-RXN_Light_c','PGLUCISOM-RXN_Light_c'],
                 ['PGLUCISOM-RXN_Light_p','PGLUCISOM-RXN_Light_p'],
                 ['6PFRUCTPHOS-RXN_Light_c','6PFRUCTPHOS-RXN_Dark_c'],
                 ['6PFRUCTPHOS-RXN_Light_p','6PFRUCTPHOS-RXN_Dark_p'],
                 ['F16ALDOLASE-RXN_Light_c','F16ALDOLASE-RXN_Dark_c'],
                 ['F16ALDOLASE-RXN_Light_p','F16ALDOLASE-RXN_Dark_p'],
                 ['TRIOSEPISOMERIZATION-RXN_Light_c','TRIOSEPISOMERIZATION-RXN_Dark_c'],
                 ['TRIOSEPISOMERIZATION-RXN_Light_p','TRIOSEPISOMERIZATION-RXN_Dark_p'],
                 ['GAPOXNPHOSPHN-RXN_Light_c','GAPOXNPHOSPHN-RXN_Dark_c'],
                 ['GAPOXNPHOSPHN-RXN_Light_p','GAPOXNPHOSPHN-RXN_Dark_p'],
                 ['PHOSGLYPHOS-RXN_Light_c','PHOSGLYPHOS-RXN_Dark_c'],
                 ['PHOSGLYPHOS-RXN_Light_p','PHOSGLYPHOS-RXN_Dark_p'],
                 ['3PGAREARR-RXN_Light_c','3PGAREARR-RXN_Dark_c'],
                 ['3PGAREARR-RXN_Light_p','3PGAREARR-RXN_Dark_p'],
                 ['2PGADEHYDRAT-RXN_Light_c','2PGADEHYDRAT-RXN_Dark_c'],
                 ['2PGADEHYDRAT-RXN_Light_p','2PGADEHYDRAT-RXN_Dark_p'],
                 ['PEPDEPHOS-RXN_Light_c','PEPDEPHOS-RXN_Dark_c'],
                 ['PEPDEPHOS-RXN_Light_p','PEPDEPHOS-RXN_Dark_p']
                ]

    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M, reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'GLYCOLYSIS']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)

    #############
    #### TCA ####
    #############

#     Pyruvate dehydrogenase
#     Citrate synthase
#     Aconitase
#     Isocitrate dehydrogenase
#     2-oxoglutarate dehydrogenase
#     Succinate thiokinase
#     Complex II
#     Fumarase

    #CHECK IF SUCCCOA-RXN IS SUCCINATE THIOKINASE RXN
    rxnIndex = [['PyruvateDH_Lt_m ','PyruvateDH_Dk_m '],
                ['PyruvateDH_Lt_p','PyruvateDH_Dk_p'],
                ['Citrate_Synthase_Lt_m', 'Citrate_Synthase_Dk_m '],
                ['Citrate_Synthase_Lt_x', 'Citrate_Synthase_Dk_x '],
                ['Aconitase_Lt_m ','Aconitase_Dk_m'],
                ['Aconitase_Lt_c','Aconitase_Dk_c'],
                ['IsocitrateDH_Lt_m','IsocitrateDH_Dk_m'],
                ['2-oxoglutarateDH_Lt_m','2-oxoglutarateDH_Dk_m'],
                ['SuccinateTK_Lt_m','SuccinateTK_Dk_m'],
                ['Fumarase_Lt_m','Fumarase_Dk_m'],
                ['Fumarase_Lt_c','Fumarase_Dk_c'],
                ['Malate_DH_Lt_m','Malate_DH_Dk_m'],
                ['Malate_DH_Lt_p','Malate_DH_Dk_p'],
                ['Malate_DH_Lt_c','Malate_DH_Dk_c'],
                ['Malate_DH_Lt_x','Malate_DH_Dk_x']
               ]

    reactions = [['PYRUVDEH-RXN_Light_m','PYRUVDEH-RXN_Dark_m'],
                 ['PYRUVDEH-RXN_Light_p','PYRUVDEH-RXN_Dark_p'],
                 ['CITSYN-RXN_Light_m','CITSYN-RXN_Dark_m'],
                 ['CITSYN-RXN_Light_x','CITSYN-RXN_Dark_x'],
                 ['ACONITATEHYDR-RXN_Light_m','ACONITATEHYDR-RXN_Dark_m'],
                 ['ACONITATEHYDR-RXN_Light_c','ACONITATEHYDR-RXN_Dark_c'],
                 ['ISOCITRATE-DEHYDROGENASE-NAD+-RXN_Light_m','ISOCITRATE-DEHYDROGENASE-NAD+-RXN_Dark_m'],
                 #include isocitrate DH in Cytosol
                 #Add PEPCARBOX-RXN_Light_c
                 ['2OXOGLUTARATEDEH-RXN_Light_m','2OXOGLUTARATEDEH-RXN_Dark_m'],
                 ['SUCCCOASYN-RXN_Light_m','SUCCCOASYN-RXN_Dark_m'],
                 ['FUMHYDR-RXN_Light_m','FUMHYDR-RXN_Dark_m'],
                 ['FUMHYDR-RXN_Light_c','FUMHYDR-RXN_Dark_c'],
                 ['MALATE-DEH-RXN_Light_m','MALATE-DEH-RXN_Dark_m'],
                 ['MALATE-DEH-RXN_Light_p','MALATE-DEH-RXN_Dark_p'],
                 ['MALATE-DEH-RXN_Light_c','MALATE-DEH-RXN_Dark_c'],
                 ['MALATE-DEH-RXN_Light_x','MALATE-DEH-RXN_Dark_x']
                ]


    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M,reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'TCA']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)

    ##############
    #### OPPP ####
    ##############

    rxnIndex = [['Hexose_P_Isomerase_Lt_p','Hexose_P_Isomerase_Dk_p '],
                ['Hexose_P_Isomerase_Lt_c','Hexose_P_Isomerase_Dk_c'],
                ['Transadolase_Lt_p','Transadolase_Dk_p'],
                ['1_Transketolase_Lt_p','1_Transketolase_Dk_p'],
                ['2_Transketolase_Lt_p','2_Transketolase_Dk_p'],
                ['Epimerase_Lt_p','Epimerase_Dk_p'],
                ['Epimerase_Lt_c','Epimerase_Dk_c'],
                ['R5P_Isomerase_Lt_p','R5P_Isomerase_Dk_p'],
                ['R5P_Isomerase_Lt_c','R5P_Isomerase_Dk_c'],
                ['G6PDH1_Lt_p','G6PDH1_Dk_p'],
                ['G6PDH1_Lt_c','G6PDH1_Dk_c'],
                ['G6PDH2_Lt_p','G6PDH2_Dk_p'],
                ['G6PDH2_Lt_c','G6PDH2_Dk_c'],
                ['GLCNATE6P-DH_Lt_c','GLCNATE6P-DH_Dk_c'],
                ['GLCNATE6P-DH_p_Lt_p','GLCNATE6P-DH_Dk_p']
                ]

    reactions = [['PGLUCISOM-RXN_Light_p','PGLUCISOM-RXN_Dark_p'],
                 ['PGLUCISOM-RXN_Light_c','PGLUCISOM-RXN_Dark_c'],
                 ['TRANSALDOL-RXN_Light_p','TRANSALDOL-RXN_Dark_p'],
                 ['1TRANSKETO-RXN_Light_p','1TRANSKETO-RXN_Dark_p'],
                 ['2TRANSKETO-RXN_Light_p','2TRANSKETO-RXN_Dark_p'],
                 ['RIBULP3EPIM-RXN_Light_p','RIBULP3EPIM-RXN_Dark_p'],
                 ['RIBULP3EPIM-RXN_Light_c','RIBULP3EPIM-RXN_Dark_c'],
                 ['RIB5PISOM-RXN_Light_p','RIB5PISOM-RXN_Dark_p'],
                 ['RIB5PISOM-RXN_Light_c','RIB5PISOM-RXN_Dark_c'],
                 ['GLU6PDEHYDROG-RXN_Light_p','GLU6PDEHYDROG-RXN_Dark_p'],
                 ['GLU6PDEHYDROG-RXN_Light_c','GLU6PDEHYDROG-RXN_Dark_c'],
                 ['6PGLUCONOLACT-RXN_Light_p','6PGLUCONOLACT-RXN_Dark_p'],
                 ['6PGLUCONOLACT-RXN_Light_c','6PGLUCONOLACT-RXN_Dark_c'],
                 ['6PGLUCONDEHYDROG-RXN_Light_c','6PGLUCONDEHYDROG-RXN_Dark_c'],
                 ['6PGLUCONDEHYDROG-RXN_Light_p','6PGLUCONDEHYDROG-RXN_Dark_p']
                ]

    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M,reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'PPP']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)

    #############
    #### ETC ####
    #############

    rxnIndex = [['Complex_I_Lt_m', 'Complex_I_Dk_m '],
                ['Complex II_Lt_m ','Complex_II_Dk_m '],
                ['Complex_III_Lt_m','Complex_III_Dk_m'],
                ['Complex_IV_Lt_m','Complex_IV_Dk_m'],
                ['AOX1','AOX1'],
                ['AOX2','AOX2']
                ]
    reactions = [['NADH-DEHYDROG-A-RXN_Light_m','NADH-DEHYDROG-A-RXN_Light_m'],
                 ['SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN_Light_m','SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN_Dark_m'],
                 ['CYTOCHROME-C-OXIDASE-RXN_Light_m','CYTOCHROME-C-OXIDASE-RXN_Dark_m'],
                 ['1.10.2.2-RXN_Light_m','1.10.2.2-RXN_Dark_m'],
                 ['RXN-6883_Light_m','RXN-6883_Dark_m'],
                 ['RXN-6884_Light_m','RXN-6884_Dark_m']
                 #Add all the RXN0-5330
                ]

    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M,reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'ETC']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)

    ######################
    #### PHOTOSYSTEMS ####
    ######################

    rxnIndex = [['PS-II_Lt_p', 'PS-II_Dk_p '],
                ['PQuinol-PCyanin-Reduc_Lt_p','PQuinol-PCyanin-Reduc_Dk_p'],
                ['PS-I_Lt_p ','PS-I_Dk_p'],
                ['Ferredoxin-Oxidase_Lt_p','Ferredoxin-Oxidase_Dk_p'],
                ['Cyclic-PS_Lt_p','Cyclic-PS_Dk_p']
                ]
    reactions = [['PSII-RXN_Light_p','PSII-RXN_Dark_p'],
                 ['PLASTOQUINOL--PLASTOCYANIN-REDUCTASE-RXN_Light_p','PLASTOQUINOL--PLASTOCYANIN-REDUCTASE-RXN_Dark_p'],
                 ['RXN490-3650_Light_p','RXN490-3650_Dark_p'],
                 ['1.18.1.2-RXN_Light_p','1.18.1.2-RXN_Dark_p'],
                 ['Ferredoxin_Plastoquinone_Reductase_Light_p','Ferredoxin_Plastoquinone_Reductase_Dark_p']#???Cyclic?
                ]

    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M,reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'PHOTOSYSTEMS']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)
    
    ###################
    #### BIOMASSES ####
    ###################

    rxnIndex = [['Sucrose_Light_biomass','Sucrose_Dark_biomass'],
                ['Alanine_Light_biomass','Alanine_Dark_biomass'],
                ['Arginine_Light_biomass','Arginine_Dark_biomass'],
                ['Aspartate_Light_biomass','Aspartate_Dark_biomass'],
                ['Glutamate_Light_biomass','Glutamate_Dark_biomass'],
                ['Glutamine_Light_biomass','Glutamine_Dark_biomass'],
                ['Glycine_Light_biomass','Glycine_Dark_biomass'],
                ['Serine_Light_biomass','Serine_Dark_biomass'],
                ['Tyrosine_Light_biomass','Tyrosine_Dark_biomass'],
                ['Histidine_Light_biomass','Histidine_Dark_biomass'],
                ['Isoleucine_Light_biomass','Isoleucine_Dark_biomass'],
                ['Leucine_Light_biomass','Leucine_Dark_biomass'],
                ['Lysine_Light_biomass','Lysine_Dark_biomass'],
                ['Methionine_Light_biomass','Methionine_Dark_biomass'],
                ['Phenylalanine_Light_biomass','Phenylalanine_Dark_biomass'],
                ['Threonine_Light_biomass','Threonine_Dark_biomass'],
                ['Tryptophan_Light_biomass','Tryptophan_Dark_biomass'],
                ['Valine_Light_biomass','Valine_Dark_biomass']
                ]
                

    reactions = [['Sucrose_Light_biomass','Sucrose_Dark_biomass'],
                ['Alanine_Light_biomass','Alanine_Dark_biomass'],
                ['Arginine_Light_biomass','Arginine_Dark_biomass'],
                ['Aspartate_Light_biomass','Aspartate_Dark_biomass'],
                ['Glutamate_Light_biomass','Glutamate_Dark_biomass'],
                ['Glutamine_Light_biomass','Glutamine_Dark_biomass'],
                ['Glycine_Light_biomass','Glycine_Dark_biomass'],
                ['Serine_Light_biomass','Serine_Dark_biomass'],
                ['Tyrosine_Light_biomass','Tyrosine_Dark_biomass'],
                ['Histidine_Light_biomass','Histidine_Dark_biomass'],
                ['Isoleucine_Light_biomass','Isoleucine_Dark_biomass'],
                ['Leucine_Light_biomass','Leucine_Dark_biomass'],
                ['Lysine_Light_biomass','Lysine_Dark_biomass'],
                ['Methionine_Light_biomass','Methionine_Dark_biomass'],
                ['Phenylalanine_Light_biomass','Phenylalanine_Dark_biomass'],
                ['Threonine_Light_biomass','Threonine_Dark_biomass'],
                ['Tryptophan_Light_biomass','Tryptophan_Dark_biomass'],
                ['Valine_Light_biomass','Valine_Dark_biomass']
                ]
                
    M1_rxn, M2_rxn, M_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M,reactions, rxnIndex)
    tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn,'M':M_rxn},index = indexes)
    tempGroup = [tempDataframe,'BIOMASSES']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)
    


    ##############
    #### M1M2 ####
    ##############
    

    rxnIndex = [['Sucrose_Light_M1M2','Sucrose_Dark_M1M2'],
                ['GLY_Light_M1M2','GLY_Dark_M1M2'],
                ['MET_Light_M1M2','MET_Dark_M1M2'],
                ['LEU_Light_M1M2','LEU_Dark_M1M2'],
                ['HIS_Light_M1M2','HIS_Dark_M1M2'],
                ['VAL_Light_M1M2','VAL_Dark_M1M2'],
                ['ILE_Light_M1M2','ILE_Dark_M1M2'],
                ['L-ALPHA-ALANINE_Light_M1M2','L-ALPHA-ALANINE_Dark_M1M2'],
                ['L-ASPARTATE_Light_M1M2','L-ASPARTATE_Dark_M1M2'],
                ['SER_Light_M1M2','SER_Dark_M1M2'],
                ['TYR_Light_M1M2','TYR_Dark_M1M2'],
                ['LYS_Light_M1M2','LYS_Dark_M1M2'],
                ['PHE_Light_M1M2','PHE_Dark_M1M2'],
                ['ARG_Light_M1M2','ARG_Dark_M1M2'],
                ['TRP_Light_M1M2','TRP_Dark_M1M2'],
                ['GLT_Light_M1M2','GLT_Dark_M1M2'],
                ['ASN_Light_M1M2','ASN_Dark_M1M2'],
                ['THR_Light_M1M2','THR_Dark_M1M2']
               ]
    reactions = [['Sucrose_Light_M1M2','Sucrose_Dark_M1M2'],
                ['GLY_Light_M1M2','GLY_Dark_M1M2'],
                ['MET_Light_M1M2','MET_Dark_M1M2'],
                ['LEU_Light_M1M2','LEU_Dark_M1M2'],
                ['HIS_Light_M1M2','HIS_Dark_M1M2'],
                ['VAL_Light_M1M2','VAL_Dark_M1M2'],
                ['ILE_Light_M1M2','ILE_Dark_M1M2'],
                ['L-ALPHA-ALANINE_Light_M1M2','L-ALPHA-ALANINE_Dark_M1M2'],
                ['L-ASPARTATE_Light_M1M2','L-ASPARTATE_Dark_M1M2'],
                ['SER_Light_M1M2','SER_Dark_M1M2'],
                ['TYR_Light_M1M2','TYR_Dark_M1M2'],
                ['LYS_Light_M1M2','LYS_Dark_M1M2'],
                ['PHE_Light_M1M2','PHE_Dark_M1M2'],
                ['ARG_Light_M1M2','ARG_Dark_M1M2'],
                ['TRP_Light_M1M2','TRP_Dark_M1M2'],
                ['GLT_Light_M1M2','GLT_Dark_M1M2'],
                ['ASN_Light_M1M2','ASN_Dark_M1M2'],
                ['THR_Light_M1M2','THR_Dark_M1M2']
               ]
    

    M1M2_rxn, indexes = prepareDataWithCustomIndex(sol_M1M2, sol_M, reactions, rxnIndex, M1M2only=True)
    tempDataframe = pd.DataFrame({'M1M2':M1M2_rxn},index = indexes)
    tempGroup = [tempDataframe,'M1M2']
    print_groups.append(tempGroup)
    excel_groups.append(tempDataframe)


    ################
    #### Others ####
    ################
    #CURRENTLY NOT WORKING
    if reacList!=None:
        M1_rxn, M2_rxn, indexes = prepareDataForVisualization(reactions)
        tempDataframe = pd.DataFrame({'M1':M1_rxn,'M2':M2_rxn},index = indexes)
        tempGroup = [tempDataframe,'OTHERS']

    #### DISPLAYING ALL THE DATA IN CATEGORIES ####
    
    totalFlux = totalAbsFlux(sol_M1M2)
    print 'Total Flux:', totalFlux
    photonDiff = sol_M1M2['Photon_Light_tx_M1'] + sol_M1M2['Photon_Light_tx_M2'] - sol_M['Photon_Light_tx']
    print 'M1M2-M Photon Diff:', photonDiff
    print '\n'
    for group in range(len(print_groups)):
        print print_groups[group][1]
        print print_groups[group][0]
        print '\n'

    #### If write data is true ####
    if writeData:
        result = pd.concat(excel_groups)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('panda_test.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
#         gly = pd.DataFrame({'Categories':['glycolysis']},index)
#         gly = pd.concat(gly)
#         gly.to_excel(writer, sheet_name='Sheet1')

        result.to_excel(writer, sheet_name='Sheet1',startcol = 1)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
    
    return pd.concat(excel_groups)


# ### Misc functions

# In[ ]:

def notInList(element, alist):
    for i in alist:
        if element == i:
            return False
    return True

def pltFluxChange(df1, df2):
    
    rxn = df1.index
    M1diff = df2['M1'] - df1['M1']
    M2diff = df2['M2'] - df1['M2']
    M1M2diff = df2['M1M2'] - df1['M1M2']


    tempdf = pd.DataFrame({'x':rxn,'y':M1diff})
    M1data = go.Bar(
            x=tempdf['x'],
            y=tempdf['y'],
            name = 'M1'
        )

    tempdf2 = pd.DataFrame({'x':rxn,'y':M2diff})
    M2data = go.Bar(
            x=tempdf2['x'], 
            y=tempdf2['y'],
            name = 'M2'
        )
    
    tempdf3 = pd.DataFrame({'x':rxn,'y':M1M2diff})
    M1M2data = go.Bar(
            x=tempdf3['x'], 
            y=tempdf3['y'],
            name = 'M1M2'
        )

    layout = go.Layout(
        barmode='group'

    )
    
    data = [M1data,M2data,M1M2data]
    fig = go.Figure(data=data, layout=layout)
    fig['layout'].update(title='Changes between Intermediates')
    iplot(fig)

def pltFluxChangeWithOriginal(df):
    
    rxn = df.index
    M1diff = df['M1'] - df['M']
    M2diff = df['M2'] - df['M']



    tempdf = pd.DataFrame({'x':rxn,'y':M1diff})
    M1data = go.Bar(
            x=tempdf['x'],
            y=tempdf['y'],
            name = 'M1diff'
        )

    tempdf2 = pd.DataFrame({'x':rxn,'y':M2diff})
    M2data = go.Bar(
            x=tempdf2['x'], 
            y=tempdf2['y'],
            name = 'M2diff'
        )


    layout = go.Layout(
        barmode='group'

    )

    # fig = tools.make_subplots(rows=2, cols=1)

    fig = tools.make_subplots(rows = 2, cols = 1, shared_xaxes=True, vertical_spacing = 0
                             )

    fig.append_trace(M1data, 1, 1)
    fig.append_trace(M2data, 2, 1)
    fig['layout'].update(title='Changes from original model M')

    iplot(fig, filename='test1')



