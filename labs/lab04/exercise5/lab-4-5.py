<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab-4-5"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2026-07-13 09:16:20 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0xMzswNzo1ODowNiBBTTsyNzQ3"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUozOVAxTlQ7MjAyNi0wNy0xMzswOToxNjoyMCBBTTsxOzI4NDc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="scoreA" type="Integer" array="False" size=""/>
            <declare name="scoreB" type="Integer" array="False" size=""/>
            <input variable="scoreA"/>
            <input variable="scoreB"/>
            <declare name="pointsA" type="Integer" array="False" size=""/>
            <declare name="pointsB" type="Integer" array="False" size=""/>
            <if expression="scoreA&gt;scoreB">
                <then>
                    <assign variable="pointsA" expression="3"/>
                    <assign variable="pointsB" expression="0"/>
                    <if expression="scoreB==0">
                        <then>
                            <assign variable="pointsA" expression="pointsA+1"/>
                        </then>
                        <else/>
                    </if>
                </then>
                <else>
                    <if expression="scoreB&gt;scoreA">
                        <then>
                            <assign variable="pointsB" expression="3"/>
                            <assign variable="pointsA" expression="0"/>
                            <if expression="scoreA==0">
                                <then>
                                    <assign variable="pointsB" expression="pointsB+1"/>
                                </then>
                                <else/>
                            </if>
                        </then>
                        <else>
                            <assign variable="pointsA" expression="1"/>
                            <assign variable="pointsB" expression="1"/>
                            <if expression="scoreA==0">
                                <then>
                                    <assign variable="pointsA" expression="pointsA+1"/>
                                    <assign variable="pointsB" expression="pointsB+1"/>
                                </then>
                                <else/>
                            </if>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="pointsA" newline="True"/>
            <output expression="pointsB" newline="True"/>
        </body>
    </function>
</flowgorithm>
