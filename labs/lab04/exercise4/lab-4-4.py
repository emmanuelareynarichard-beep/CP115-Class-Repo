<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab-4-4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2026-07-13 08:38:08 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0xMzswNzo0Nzo0OCBBTTsyNzUx"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0xMzswODozODowOCBBTTsyOzI4NTc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="weight" type="Real" array="False" size=""/>
            <declare name="ticketPrice" type="Real" array="False" size=""/>
            <input variable="weight"/>
            <input variable="ticketPrice"/>
            <declare name="finalPrice" type="Real" array="False" size=""/>
            <if expression="weight=0">
                <then>
                    <assign variable="finalPrice" expression="ticketPrice-10.00"/>
                </then>
                <else>
                    <if expression="weight&gt;=15">
                        <then>
                            <assign variable="finalPrice" expression="((weight-15)*4.00)+ticketPrice"/>
                        </then>
                        <else>
                            <assign variable="finalPrice" expression="ticketPrice"/>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="finalPrice" newline="True"/>
        </body>
    </function>
</flowgorithm>
