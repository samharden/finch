#!/usr/bin/env python


email_body_new = """
<!doctype html>
<html>
  <head>
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Finch Notification</title>
    <style>

    @media only screen and (max-width: 620px) {{
      table[class=body] h1 {{
        font-size: 28px ;
        margin-bottom: 10px ;
      }}
      table[class=body] p,
            table[class=body] ul,
            table[class=body] ol,
            table[class=body] td,
            table[class=body] span,
            table[class=body] a {{
        font-size: 16px ;
      }}
      table[class=body] .wrapper,
            table[class=body] .article {{
        padding: 10px ;
      }}
      table[class=body] .content {{
        padding: 0 ;
      }}
      table[class=body] .container {{
        padding: 0 ;
        width: 100% ;
      }}
      table[class=body] .main {{
        border-left-width: 0 ;
        border-radius: 0 ;
        border-right-width: 0 ;
      }}
      table[class=body] .btn table {{
        width: 100% ;
      }}
      table[class=body] .btn a {{
        width: 100% ;
      }}
      table[class=body] .img-responsive {{
        height: auto ;
        max-width: 100% ;
        width: auto ;
      }}
    }}
    /* -------------------------------------
        PRESERVE THESE STYLES IN THE HEAD
    ------------------------------------- */
    @media all {{
      .ExternalClass {{
        width: 100%%;
      }}
      .ExternalClass,
            .ExternalClass p,
            .ExternalClass span,
            .ExternalClass font,
            .ExternalClass td,
            .ExternalClass div {{
        line-height: 100%%;
      }}
      .apple-link a {{
        color: inherit ;
        font-family: inherit ;
        font-size: inherit ;
        font-weight: inherit ;
        line-height: inherit ;
        text-decoration: none ;
      }}
      .btn-primary table td:hover {{
        background-color: #34495e ;

      }}
      .btn-primary a:hover {{
        background-color: #34495e ;
        border-color: #34495e ;
      }}
    }}
    </style>
  </head>
  <body class="" style="background-color: #f6f6f6; font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
    <table border="0" cellpadding="0" cellspacing="0" class="body" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background-color: #f6f6f6;">
      <tr>
        <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;">&nbsp;</td>
        <td class="container" style="font-family: sans-serif; font-size: 14px; vertical-align: top; display: block; Margin: 0 auto; max-width: 580px; padding: 10px; width: 580px;">
          <div class="content" style="box-sizing: border-box; display: block; Margin: 0 auto; max-width: 580px; padding: 10px;">
            <h2 style="font-family: sans-serif; font-size: 16px; font-weight: normal; margin: 0; Margin-bottom: 5px; text-align:center">
            <img src="https://www.finch-km.com/static/images/greyfinch.png" style="width:26px"><br>Finch-KM</h2>

              <span class="preheader" style="color: transparent; display: none; height: 0; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all; visibility: hidden; width: 0;">Your discussion has been posted.</span>
              <table class="main" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background: #ffffff; border-radius: 3px;">


                <tr>
                  <td class="wrapper" style="font-family: sans-serif; font-size: 14px; vertical-align: top; box-sizing: border-box; padding: 10px;">
                    <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;">
                      <tr>
                        <!-- <td style="font-family: sans-serif; font-size: 14px; vertical-align: top; horizontal-align: center"> -->
                        <h3>New Discussion on Finch</h3>
                          <p>Area: {0} </p>
                          <p>Posted by: {1}</p>
                          <br>
                          <p>{2}</p>

  <tr>
    <td style="font-family: sans-serif; font-size: 14px; vertical-align: top; background-color: #3498db; border-radius: 5px; text-align: center;">

      <a href="{3}" target="_blank" style="display: inline-block; color: #ffffff; background-color: #3498db; border: solid 1px #3498db; border-radius: 5px; box-sizing: border-box; cursor: pointer; text-decoration: none; font-size: 14px; font-weight: bold; margin: 0; padding: 12px 25px; text-transform: capitalize; border-color: #3498db;">
        View post.</a> </td><br></br>
  </tr>
</tbody>

           </td>
         </tr>
       </table>
     </td>
   </tr>

 <!-- END MAIN CONTENT AREA -->
</table></span><br>



                    <!-- START FOOTER -->
                    <div class="footer" style="clear: both; Margin-top: 10px; text-align: center; width: 100%;">
                      <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;">
                        <tr>
                          <td class="content-block" style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; font-size: 12px; color: #999999; text-align: center;">
                            <span class="apple-link" style="color: #999999; font-size: 12px; text-align: center;">
                              Finch-KM</span>

                          </td>
                        </tr>
                        <tr>
                          <td class="content-block powered-by" style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; font-size: 12px; color: #999999; text-align: center;">
                            <a href="https://www.lancorp.co">Powered by Lancorp</a>
                          </td>
                        </tr>
                      </table>
                    </div>
                    <!-- END FOOTER -->

                  <!-- END CENTERED WHITE CONTAINER -->
                  </div>
                </td>
                <!-- <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;">&nbsp;</td> -->
              <!-- </tr> -->
            </table>
          </body>
        </html>

"""
