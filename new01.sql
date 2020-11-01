SELECT ("public"."router_messagetask"."data" -> 'end')::TEXT as datetime ,
        CASE WHEN "public"."router_messagetask"."trigger_id" = 37 THEN 'пришел в ' || ("public"."router_messagetask"."data" -> 'type_name')::TEXT || ', ' || ("public"."router_messagetask"."data" -> 'end')::TEXT
            WHEN "public"."router_messagetask"."trigger_id" = 38 THEN 'вышел из ' || ("public"."router_messagetask"."data" -> 'type_name')::TEXT || ', ' || ("public"."router_messagetask"."data" -> 'end')::TEXT
            WHEN "public"."router_messagetask"."trigger_id" = 39 THEN 'встретил новые сутки в ' || ("public"."router_messagetask"."data" -> 'type_name')::TEXT || ', ' || ("public"."router_messagetask"."data" -> 'end')::TEXT
            WHEN "public"."router_messagetask"."trigger_id" = 40 THEN 'приехал в район/город/страну ' || ("public"."router_messagetask"."data" -> 'city')::TEXT || ', ' || ("public"."router_messagetask"."data" -> 'end')::TEXT
            WHEN "public"."router_messagetask"."trigger_id" = 41 THEN 'был в месте ' || ("public"."router_messagetask"."data" -> 'place_name')::TEXT || ', с ' || ("public"."router_messagetask"."data" -> 'begin')::TEXT || ' до ' || ("public"."router_messagetask"."data" -> 'end')::TEXT
        END as m_text,
        "public"."router_messagetask"."event" AS "events"
FROM "public"."router_messagetask"
WHERE ("public"."router_messagetask"."trigger_id" IN (37, 38, 39, 40, 41)
   AND "public"."router_messagetask"."user_id" = 153692 and (NOT "public"."router_messagetask"."data" IS NULL)) and "public"."router_messagetask"."is_duplicated" = false
GROUP BY datetime, m_text, events
ORDER BY datetime DESC, m_text, events
