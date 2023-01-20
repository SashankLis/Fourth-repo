import Snowflake as sf


def sales_mth():

    #truncate tmp table sales_agg_month

    # truncate_tmp_sales_mth = '''
    #                             TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_SALES_MTH
    #                            '''
    #
    # sf.execute_query(truncate_tmp_sales_mth)

    #load tmp table sales_agg_month


    # load_temp_sales_mth = '''
    #                         INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_SALES_MTH(
    #                         SLS_KY,
    #                         SLS_ID, MTH_KY,STORE_KY,
    #                         PDT_KY, CUSTOMER_KY,TRANSACTION_TIME,
    #                         QTY,AMT,DSCNT
    #                         )
    #                         SELECT SLS_KY,
    #                         SLS_ID,
    #                         MONTH(TRANSACTION_TIME),
    #                         LOCN_KY,PDT_KY,CUSTOMER_KY,
    #                         TRANSACTION_TIME,QTY,AMT,DSCNT
    #                         FROM BHATBHATENI.SASHANK_TGT.TGT_SALES
    #                         '''
    #
    # sf.execute_query(load_temp_sales_mth)

    #update target table sales_agg_month


    # update_tgt_sales_mth = '''
    #                         UPDADTE BHATBHATENI.SASHANK_TGT.TGT_SALES_AGG T1
    #                         SET T1.LOCN_KY = T2.STORE_KY,
    #                         T1.PDT_KY = T2.PDT_KY,
    #                         T1.CUSTOMER_KY = T2.CUSTOMER_KY,
    #                         T1.QTY = T1.QTY + T2.QTY,
    #                         T1.AMT = T1.QTY + T2.AMT,
    #                         T1.DSCNT = T1.DSCNT + T2.DSCNT,
    #                         ROW_UPDT_TMS = LOCALTIMESTAMP
    #                         FROM BHATBHATENI.SASHANK_TMP.TMP_SALES T2
    #                         WHERE T1.SLS_KY = T2.SLS_KY
    #                         '''
    #
    # sf.execute_query(update_tgt_sales_mth)

    #load target table sales_agg_month

    load_tgt_sales_mth = '''
                            INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_SALES_MTH(
                            SLS_KY,
                            SLS_ID,MTH_KY,LOCN_KY,PDT_KY,CUSTOMER_KY,
                            TRANSACTION_TIME,QTY,AMT,DSCNT,OPEN_CLOSE_CD,
                            ROW_INSRT_TMS, ROW_UPDT_TMS
                            )
                            SELECT SLS_KY,SLS_ID,MTH_KY,STORE_KY,PDT_KY,CUSTOMER_KY,TRANSACTION_TIME,
                            QTY,AMT,DSCNT,1,LOCALTIMESTAMP,LOCALTIMESTAMP
                            FROM  BHATBHATENI.SASHANK_TMP.TMP_SALES_MTH
                            WHERE SLS_ID NOT IN (SELECT SLS_ID FROM BHATBHATENI.SASHANK_TGT.TGT_SALES_MTH)
                            '''
    sf.execute_query(load_tgt_sales_mth)