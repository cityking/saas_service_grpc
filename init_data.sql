--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.2
-- Dumped by pg_dump version 9.6.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ali_pay; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE ali_pay (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    app_id character varying(20) NOT NULL,
    notify_url character varying(100),
    ali_pub_key text,
    app_pri_key text,
    app_pub_key text
);


ALTER TABLE ali_pay OWNER TO cityking;

--
-- Name: ali_pay_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE ali_pay_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ali_pay_id_seq OWNER TO cityking;

--
-- Name: ali_pay_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE ali_pay_id_seq OWNED BY ali_pay.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO cityking;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO cityking;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO cityking;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO cityking;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO cityking;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO cityking;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO cityking;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO cityking;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO cityking;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO cityking;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO cityking;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO cityking;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO cityking;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO cityking;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO cityking;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO cityking;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO cityking;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO cityking;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO cityking;

--
-- Name: msg_business; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE msg_business (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    msg_num integer NOT NULL
);


ALTER TABLE msg_business OWNER TO cityking;

--
-- Name: msg_business_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE msg_business_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE msg_business_id_seq OWNER TO cityking;

--
-- Name: msg_business_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE msg_business_id_seq OWNED BY msg_business.id;


--
-- Name: msg_charge_package; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE msg_charge_package (
    id integer NOT NULL,
    title character varying(30),
    price double precision NOT NULL,
    charge_num integer NOT NULL
);


ALTER TABLE msg_charge_package OWNER TO cityking;

--
-- Name: msg_charge_package_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE msg_charge_package_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE msg_charge_package_id_seq OWNER TO cityking;

--
-- Name: msg_charge_package_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE msg_charge_package_id_seq OWNED BY msg_charge_package.id;


--
-- Name: msg_order; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE msg_order (
    id integer NOT NULL,
    order_no character varying(20) NOT NULL,
    charge_num integer NOT NULL,
    price double precision NOT NULL,
    pay_type integer NOT NULL,
    state integer NOT NULL,
    business_id integer NOT NULL,
    create_time timestamp with time zone NOT NULL
);


ALTER TABLE msg_order OWNER TO cityking;

--
-- Name: msg_order_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE msg_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE msg_order_id_seq OWNER TO cityking;

--
-- Name: msg_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE msg_order_id_seq OWNED BY msg_order.id;


--
-- Name: msg_pay_info; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE msg_pay_info (
    id integer NOT NULL,
    pay_type integer NOT NULL,
    app_id character varying(50) NOT NULL,
    business_id integer NOT NULL
);


ALTER TABLE msg_pay_info OWNER TO cityking;

--
-- Name: msg_pay_info_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE msg_pay_info_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE msg_pay_info_id_seq OWNER TO cityking;

--
-- Name: msg_pay_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE msg_pay_info_id_seq OWNED BY msg_pay_info.id;


--
-- Name: msg_record; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE msg_record (
    id integer NOT NULL,
    phone character varying(20) NOT NULL,
    content character varying(500) NOT NULL,
    create_time timestamp with time zone NOT NULL,
    state integer NOT NULL,
    business_id integer NOT NULL
);


ALTER TABLE msg_record OWNER TO cityking;

--
-- Name: msg_record_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE msg_record_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE msg_record_id_seq OWNER TO cityking;

--
-- Name: msg_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE msg_record_id_seq OWNED BY msg_record.id;


--
-- Name: weixin_pay; Type: TABLE; Schema: public; Owner: cityking
--

CREATE TABLE weixin_pay (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    app_id character varying(20) NOT NULL,
    mch_id character varying(20) NOT NULL,
    mch_key character varying(50) NOT NULL,
    notify_url character varying(100),
    cert_key character varying(100),
    cert character varying(100)
);


ALTER TABLE weixin_pay OWNER TO cityking;

--
-- Name: weixin_pay_id_seq; Type: SEQUENCE; Schema: public; Owner: cityking
--

CREATE SEQUENCE weixin_pay_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE weixin_pay_id_seq OWNER TO cityking;

--
-- Name: weixin_pay_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cityking
--

ALTER SEQUENCE weixin_pay_id_seq OWNED BY weixin_pay.id;


--
-- Name: ali_pay id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY ali_pay ALTER COLUMN id SET DEFAULT nextval('ali_pay_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: msg_business id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_business ALTER COLUMN id SET DEFAULT nextval('msg_business_id_seq'::regclass);


--
-- Name: msg_charge_package id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_charge_package ALTER COLUMN id SET DEFAULT nextval('msg_charge_package_id_seq'::regclass);


--
-- Name: msg_order id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_order ALTER COLUMN id SET DEFAULT nextval('msg_order_id_seq'::regclass);


--
-- Name: msg_pay_info id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_pay_info ALTER COLUMN id SET DEFAULT nextval('msg_pay_info_id_seq'::regclass);


--
-- Name: msg_record id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_record ALTER COLUMN id SET DEFAULT nextval('msg_record_id_seq'::regclass);


--
-- Name: weixin_pay id; Type: DEFAULT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY weixin_pay ALTER COLUMN id SET DEFAULT nextval('weixin_pay_id_seq'::regclass);


--
-- Data for Name: ali_pay; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY ali_pay (id, name, app_id, notify_url, ali_pub_key, app_pri_key, app_pub_key) FROM stdin;
1	喵哆旺	2018091261383224	http://114.55.85.57:9000/pay/alipay	-----BEGIN PUBLIC KEY-----\r\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs+k3TF6xwweK1g87ydXpJb3jhLHCPuYanMtPdcnN5j8it2g4mJ4Z/LS50mwUi3cmS5KX1oy1RJ2Q4zgIKpen4jO0pcUGqx5UwW/auaoqAP6YA4DvSnYfTVhC2wT0PdbUQNMzPz+VOOwBJNwf0A97UCR05u5GnHkjGvaAC9JawlAM1UD+VjJmQWbf+e3giI3L0pGj4otoyxcGdUpyw4zmpUwpAJBI9sH2pvk1kOTn5UBC+zTV2kEnfkX6PH/ge04WKym8zcs7JzMD4TeZ5najsOMdtp5OwVbjD6TkOfyfA/J6lMyjsxRM9Tn6m9MXGNNrYCbkeNFRWnLz1W5Q3+lrQQIDAQAB\r\n-----END PUBLIC KEY-----	-----BEGIN RSA PRIVATE KEY-----\r\nMIIEpAIBAAKCAQEAs+k3TF6xwweK1g87ydXpJb3jhLHCPuYanMtPdcnN5j8it2g4mJ4Z/LS50mwUi3cmS5KX1oy1RJ2Q4zgIKpen4jO0pcUGqx5UwW/auaoqAP6YA4DvSnYfTVhC2wT0PdbUQNMzPz+VOOwBJNwf0A97UCR05u5GnHkjGvaAC9JawlAM1UD+VjJmQWbf+e3giI3L0pGj4otoyxcGdUpyw4zmpUwpAJBI9sH2pvk1kOTn5UBC+zTV2kEnfkX6PH/ge04WKym8zcs7JzMD4TeZ5najsOMdtp5OwVbjD6TkOfyfA/J6lMyjsxRM9Tn6m9MXGNNrYCbkeNFRWnLz1W5Q3+lrQQIDAQABAoIBAB/501o/elivfn2NN5Mn8chDd6yd62hCfXhgqj7FH1NM5V6zp1t4viWr+Vrs2rnu8197LoFzgMQxPQ8lZk4rpisOBY1w9z5ypZ27w6Q8GjsTBPGaeO1DEU0t4rQKrV5QUGk1IGadZmg3ifyDIyRXnBMiZ6SjtOkanqKsLRXszTS7uTebPwNVuSKwLh06OAkbjsEeoYyxJJ8aOZlYAtWqjrnPf/gWClVFWcx68GYfPmMpg+ise/QSrsJX6oMfZqlJXSa5XIOcRxe9auxFXsGmWSVEU3R9uOpENCgKh2xnewkbafWrEqeGr1Vl1BMbQZs9QrSSUe9TJpugnuskvb8q9gECgYEA3fjwYToX4rl66LW+2LX9iPBrh6GUcmf4EjLk5RNiQoQ0DB7X2+Sx9KRlazi+makyrHn+IDm3uI1BgEncgwSivGP5k+30G60+yFQKQPedLjPGV9KNRM4rfhutUgbxGgMUcTRvhG8NWJPY5MYbyluAbhKL/+ElDKaqqpwMp/HwWy8CgYEAz32fls+xGMvv0P5fy0QRJLb0Hh1jl8nT3J7YRlrF+SHWI796e5dYHcAC+tk2Yd+/Xddb4ewr1Skib4HkjoDd2LignbAssJ5tJCE284EF4YqH1YVygKGmgYTgBb1EUrRq+u9fwJ1+AzxXu/fXMjkhGb8Tt4ua6D7gUWe3+FDyRI8CgYEAovwbvLhEO5THm8F/bW5LyFYIDqHk9xBCRVKbYVyXRJIACXpIM0y8Ig7n7Q/QW9GxxJUatJzMurT1iHYzdPxdZYjfA/Cv0famZ7/Ve5iVEAyyMWAHnKLpqoI2BEnWlKv4QZsn2w0TtptwoaKZWz9OkQQLSgoOAzkJjZZhcJukSb8CgYEAghnN6F1AOUEelRf67tQ2P6Qr+3oICZP2sP40tCCUw/rQb8fPQBGModLUy39JVyNZtbikl0tjzJunSO3UZvosoIhbxaRC0Vf1LVNaRmLfUiVvuJWdT0SMx+eOJGshnQ4dikxv6LGX4uWCSY1EtOwXcjJaZZs2vWs3cjOrqhrvXccCgYBhC+v08KIdw4OhCge0uKqIYJO7M/L7s33AeE594yGC1pAlTFsjMUlAG7j3a4yc/O1bKm4zzwOSk5Y/cjVSuE19+VEhdI3AVQ/xjnOiFoUmFImdjL4fQXyS4RHn97cU4N+FkqhMNX+jUzf6TBxISNfgs6jccuxMzAgLcUufh1gymA==\r\n-----END RSA PRIVATE KEY-----	-----BEGIN PUBLIC KEY-----\r\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp6dM7yXu9yBdsmwwZB6Kqwj/vNldnyaib7FiDc7m3ExpHTsMFcwlpB4SSWL/rqx6oQamda3k8ji//PQdBK2DoQTwdGTWG/oIndw78sdn+kL9UTH5ZGtOfoBI0lPMj2vDazGBoWCjqZ4mzWSb5lXEwKqFUlO8Gtzt0xwBuKCQxYOwjWAjmnVS0ZoIURFALfqc8n9r3y0nUCB3DaFcLckRr1mWniYyH3CvpciOL1JDis9M0i/5ZeY+I1nTxzzk8+oTD/vB20SBcPBfRGf6uDkd0yN/fFKVt3/QvxncGxORQ+oUz+KihSJXsQYiU6F4mHqIFBsFN9r15U/le1frPNjc0QIDAQAB\r\n-----END PUBLIC KEY-----
\.


--
-- Name: ali_pay_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('ali_pay_id_seq', 1, true);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add 微信支付	7	add_weixinpay
20	Can change 微信支付	7	change_weixinpay
21	Can delete 微信支付	7	delete_weixinpay
22	Can add 商户	8	add_business
23	Can change 商户	8	change_business
24	Can delete 商户	8	delete_business
25	Can add 充值套餐	9	add_chargepackage
26	Can change 充值套餐	9	change_chargepackage
27	Can delete 充值套餐	9	delete_chargepackage
28	Can add 短信记录	10	add_msgrecord
29	Can change 短信记录	10	change_msgrecord
30	Can delete 短信记录	10	delete_msgrecord
31	Can add 订单	11	add_order
32	Can change 订单	11	change_order
33	Can delete 订单	11	delete_order
34	Can add 支付信息	12	add_payinfo
35	Can change 支付信息	12	change_payinfo
36	Can delete 支付信息	12	delete_payinfo
37	Can add 支付宝支付	13	add_alipay
38	Can change 支付宝支付	13	change_alipay
39	Can delete 支付宝支付	13	delete_alipay
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('auth_permission_id_seq', 39, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$100000$b9BCVLmacQpc$Sd+OnUy8Bq9LgE4fWUeYpxqS+tg1mh780h4bbyMI7BM=	2019-07-10 16:49:23.382637+08	t	cityking				t	t	2019-06-19 11:22:48.272675+08
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-06-19 11:30:21.475945+08	1	喵哆旺	1	[{"added": {}}]	7	1
2	2019-06-19 11:46:21.748097+08	1	喵哆旺	2	[{"changed": {"fields": ["notify_url"]}}]	7	1
3	2019-06-19 11:47:52.703815+08	1	喵哆旺	2	[]	7	1
4	2019-06-19 11:52:43.823134+08	1	喵哆旺	2	[{"changed": {"fields": ["notify_url"]}}]	7	1
5	2019-06-19 11:58:33.238271+08	1	喵哆旺	2	[{"changed": {"fields": ["mch_key"]}}]	7	1
6	2019-06-20 11:09:39.146215+08	1	喵哆旺	2	[{"changed": {"fields": ["cert_key", "cert"]}}]	7	1
7	2019-07-10 16:50:00.508509+08	1	喵哆旺	1	[{"added": {}}]	8	1
8	2019-07-10 16:51:10.273377+08	1	10元200条	1	[{"added": {}}]	9	1
9	2019-07-10 16:51:36.941824+08	2	100元3000条	1	[{"added": {}}]	9	1
10	2019-07-10 16:52:35.432781+08	3	200元10000条	1	[{"added": {}}]	9	1
11	2019-07-10 16:53:11.712705+08	1	PayInfo object (1)	1	[{"added": {}}]	12	1
12	2019-07-10 16:54:11.366153+08	1	PayInfo object (1)	2	[]	12	1
13	2019-07-12 16:42:56.319056+08	1	喵哆旺	1	[{"added": {}}]	13	1
14	2019-07-12 16:47:14.222012+08	1	喵哆旺	2	[{"changed": {"fields": ["ali_pub_key", "app_pri_key", "app_pub_key"]}}]	13	1
15	2019-07-12 16:47:21.298216+08	1	喵哆旺	2	[]	13	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 15, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	pay_app	weixinpay
8	message_app	business
9	message_app	chargepackage
10	message_app	msgrecord
11	message_app	order
12	message_app	payinfo
13	pay_app	alipay
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('django_content_type_id_seq', 13, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-06-19 11:22:22.95702+08
2	auth	0001_initial	2019-06-19 11:22:23.104024+08
3	admin	0001_initial	2019-06-19 11:22:23.155369+08
4	admin	0002_logentry_remove_auto_add	2019-06-19 11:22:23.169962+08
5	contenttypes	0002_remove_content_type_name	2019-06-19 11:22:23.225131+08
6	auth	0002_alter_permission_name_max_length	2019-06-19 11:22:23.23352+08
7	auth	0003_alter_user_email_max_length	2019-06-19 11:22:23.252783+08
8	auth	0004_alter_user_username_opts	2019-06-19 11:22:23.27431+08
9	auth	0005_alter_user_last_login_null	2019-06-19 11:22:23.2938+08
10	auth	0006_require_contenttypes_0002	2019-06-19 11:22:23.29966+08
11	auth	0007_alter_validators_add_error_messages	2019-06-19 11:22:23.321379+08
12	auth	0008_alter_user_username_max_length	2019-06-19 11:22:23.342865+08
13	auth	0009_alter_user_last_name_max_length	2019-06-19 11:22:23.362323+08
14	pay_app	0001_initial	2019-06-19 11:22:23.379417+08
15	sessions	0001_initial	2019-06-19 11:22:23.400198+08
16	pay_app	0002_auto_20190619_0330	2019-06-19 11:30:15.019499+08
17	pay_app	0003_auto_20190619_0351	2019-06-19 11:51:47.981446+08
18	pay_app	0004_auto_20190619_0357	2019-06-19 11:57:37.746842+08
19	pay_app	0005_auto_20190620_0308	2019-06-20 11:08:27.441711+08
20	message_app	0001_initial	2019-07-10 16:30:05.679036+08
21	pay_app	0006_alipay	2019-07-12 16:33:46.217725+08
22	pay_app	0007_auto_20190712_0831	2019-07-12 16:33:46.235314+08
23	pay_app	0008_alipay	2019-07-12 16:33:46.283034+08
24	message_app	0002_auto_20190712_0840	2019-07-12 16:40:23.220313+08
25	pay_app	0009_auto_20190712_0840	2019-07-12 16:40:23.248157+08
26	message_app	0003_order_create_time	2019-07-16 15:40:04.505534+08
27	pay_app	0010_auto_20190716_0739	2019-07-16 15:40:04.520669+08
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('django_migrations_id_seq', 27, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
hxahikh4y34igztmsb63f0czoxt7v4zu	NGZhZGYwZWFjMzdlZWQwOGFhYWJjZDY1MGI1ZDUyZjczYzM2ZjNiMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MWU0YWY1YTA4ZmZkNjljZjlhNmFhOTVmYmMxNmRhZjhiZGMwNGZhIn0=	2019-07-03 11:24:26.702993+08
q3kxvlwksjo7outfi4jre7wszy20j8np	NGZhZGYwZWFjMzdlZWQwOGFhYWJjZDY1MGI1ZDUyZjczYzM2ZjNiMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MWU0YWY1YTA4ZmZkNjljZjlhNmFhOTVmYmMxNmRhZjhiZGMwNGZhIn0=	2019-07-24 16:49:23.386541+08
\.


--
-- Data for Name: msg_business; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY msg_business (id, name, msg_num) FROM stdin;
1	喵哆旺	110
\.


--
-- Name: msg_business_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('msg_business_id_seq', 1, true);


--
-- Data for Name: msg_charge_package; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY msg_charge_package (id, title, price, charge_num) FROM stdin;
2	100元3000条	100	3000
3	200元10000条	200	10000
1	10元200条	0.0100000000000000002	100
\.


--
-- Name: msg_charge_package_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('msg_charge_package_id_seq', 3, true);


--
-- Data for Name: msg_order; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY msg_order (id, order_no, charge_num, price, pay_type, state, business_id, create_time) FROM stdin;
4	15630062131729228	200	10	2	0	1	2019-07-16 15:40:04.356167+08
5	1563420389640286	200	10	2	0	1	2019-07-16 15:40:04.356167+08
6	1563782207720217	200	10	2	0	1	2019-07-16 15:40:04.356167+08
7	1563610348260271	200	10	2	0	1	2019-07-16 15:40:04.356167+08
8	1563232079801263	200	10	2	0	1	2019-07-16 15:40:04.356167+08
9	1563710452227756	200	10	2	0	1	2019-07-16 15:40:04.356167+08
10	1563219642335714	200	10	2	0	1	2019-07-16 15:40:04.356167+08
11	1563267229375693	200	10	2	0	1	2019-07-16 15:40:04.356167+08
12	1563891342498514	200	10	2	0	1	2019-07-16 15:40:04.356167+08
13	15635057094162931	200	10	2	0	1	2019-07-16 15:40:04.356167+08
14	1563612528071577	200	10	2	0	1	2019-07-16 15:40:04.356167+08
15	15632338998539798	200	10	1	0	1	2019-07-16 15:40:04.356167+08
16	1563445971465009	200	10	1	0	1	2019-07-16 15:40:04.356167+08
17	1564095625933972	200	10	1	0	1	2019-07-16 15:40:04.356167+08
18	1563855568741832	200	10	1	0	1	2019-07-16 15:40:04.356167+08
19	1563819873511968	200	10	1	0	1	2019-07-16 15:40:04.356167+08
20	15633983861195679	200	10	2	0	1	2019-07-16 15:40:04.356167+08
21	1564160684664168	100	0.0100000000000000002	1	0	1	2019-07-16 15:40:04.356167+08
22	15637748687637582	100	0.0100000000000000002	1	1	1	2019-07-16 15:40:04.356167+08
23	1563543123424191	100	0.0100000000000000002	2	0	1	2019-07-16 15:40:04.356167+08
24	1563471704078798	100	0.0100000000000000002	2	0	1	2019-07-16 15:40:04.356167+08
25	15633887877173738	100	0.0100000000000000002	2	1	1	2019-07-16 15:40:04.356167+08
26	1563388807423693	100	0.0100000000000000002	2	0	1	2019-07-16 15:40:04.356167+08
35	1563624807267332	100	0.0100000000000000002	2	0	1	2019-07-16 16:45:29.267989+08
36	1563711638142702	100	0.0100000000000000002	2	0	1	2019-07-16 16:46:19.143288+08
37	1563821398412212	100	0.0100000000000000002	2	0	1	2019-07-16 16:47:23.418156+08
38	1563876593972439	100	0.0100000000000000002	2	0	1	2019-07-16 16:48:10.97695+08
39	1563769947851412	100	0.0100000000000000002	2	0	1	2019-07-16 16:48:59.853787+08
40	15635651950456169	100	0.0100000000000000002	2	0	1	2019-07-16 17:01:26.049158+08
41	1563890718768427	100	0.0100000000000000002	2	0	1	2019-07-16 17:01:45.769975+08
42	1563907418647396	100	0.0100000000000000002	2	0	1	2019-07-16 17:04:26.649701+08
43	156367663570526	100	0.0100000000000000002	2	0	1	2019-07-16 17:04:41.705939+08
44	1563756336821834	100	0.0100000000000000002	2	0	1	2019-07-16 17:05:22.822467+08
45	1564093172819754	100	0.0100000000000000002	2	0	1	2019-07-16 17:12:35.824074+08
46	1563884556580149	100	0.0100000000000000002	1	0	1	2019-07-16 17:14:48.588266+08
47	15638206947726238	100	0.0100000000000000002	1	0	1	2019-07-16 17:16:06.773158+08
48	1563995899772757	100	0.0100000000000000002	1	0	1	2019-07-16 17:22:30.774973+08
49	1563755320899389	100	0.0100000000000000002	1	0	1	2019-07-16 17:22:36.899749+08
50	1564021721493442	100	0.0100000000000000002	1	0	1	2019-07-16 17:29:18.49653+08
51	1564053814839068	100	0.0100000000000000002	1	0	1	2019-07-16 17:29:23.839565+08
52	15637046586901572	100	0.0100000000000000002	2	0	1	2019-07-16 17:30:45.699059+08
53	1564029562767064	100	0.0100000000000000002	2	0	1	2019-07-16 17:45:01.768688+08
54	1563453730332046	100	0.0100000000000000002	2	0	1	2019-07-17 09:48:35.337062+08
55	1564052647242572	100	0.0100000000000000002	2	0	1	2019-07-17 10:15:53.245806+08
56	1563984121600377	100	0.0100000000000000002	2	0	1	2019-07-17 10:16:25.600763+08
57	1564118200351692	100	0.0100000000000000002	2	0	1	2019-07-17 10:17:07.352382+08
58	15638838193972101	100	0.0100000000000000002	2	0	1	2019-07-17 10:19:00.399646+08
59	1563750278640299	100	0.0100000000000000002	2	0	1	2019-07-17 10:20:09.640766+08
60	1563474667214899	100	0.0100000000000000002	1	0	1	2019-07-17 10:20:57.215655+08
61	15641956537974882	100	0.0100000000000000002	2	0	1	2019-07-17 10:25:12.799525+08
62	1564130188725282	100	0.0100000000000000002	2	0	1	2019-07-17 10:25:32.726043+08
63	1563814366612834	100	0.0100000000000000002	2	0	1	2019-07-17 10:27:27.613554+08
64	1563750157910805	100	0.0100000000000000002	2	1	1	2019-07-17 11:04:55.913296+08
65	1564068414664073	100	0.0100000000000000002	2	0	1	2019-07-17 11:06:51.664696+08
66	1564075282863322	100	0.0100000000000000002	1	0	1	2019-07-17 11:08:32.863825+08
67	1563836989536693	100	0.0100000000000000002	2	1	1	2019-07-17 11:09:09.537213+08
68	1563387503394582	100	0.0100000000000000002	1	0	1	2019-07-17 11:11:29.395103+08
69	1563781323032282	100	0.0100000000000000002	2	0	1	2019-07-17 11:13:44.034537+08
70	1563827517757051	100	0.0100000000000000002	1	0	1	2019-07-17 11:13:54.757632+08
71	1563504074572059	100	0.0100000000000000002	1	0	1	2019-07-17 11:14:11.572694+08
72	15640462821274629	100	0.0100000000000000002	2	1	1	2019-07-17 11:37:33.128402+08
73	15638573455069308	100	0.0100000000000000002	2	0	1	2019-07-17 14:11:51.50844+08
\.


--
-- Name: msg_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('msg_order_id_seq', 73, true);


--
-- Data for Name: msg_pay_info; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY msg_pay_info (id, pay_type, app_id, business_id) FROM stdin;
1	2	wx551718a402287291	1
2	1	2018091261383224	1
\.


--
-- Name: msg_pay_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('msg_pay_info_id_seq', 2, true);


--
-- Data for Name: msg_record; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY msg_record (id, phone, content, create_time, state, business_id) FROM stdin;
\.


--
-- Name: msg_record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('msg_record_id_seq', 1, false);


--
-- Data for Name: weixin_pay; Type: TABLE DATA; Schema: public; Owner: cityking
--

COPY weixin_pay (id, name, app_id, mch_id, mch_key, notify_url, cert_key, cert) FROM stdin;
1	喵哆旺	wx551718a402287291	1511406021	1125b0ffcd1a4e1b06fa169506832fb7	http://192.168.3.217:8000/pay_app/pay_callback/	uploads/cert_key/wx551718a402287291_key.pem	uploads/cert/wx551718a402287291_cert.pem
\.


--
-- Name: weixin_pay_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cityking
--

SELECT pg_catalog.setval('weixin_pay_id_seq', 1, true);


--
-- Name: ali_pay ali_pay_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY ali_pay
    ADD CONSTRAINT ali_pay_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: msg_business msg_business_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_business
    ADD CONSTRAINT msg_business_pkey PRIMARY KEY (id);


--
-- Name: msg_charge_package msg_charge_package_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_charge_package
    ADD CONSTRAINT msg_charge_package_pkey PRIMARY KEY (id);


--
-- Name: msg_order msg_order_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_order
    ADD CONSTRAINT msg_order_pkey PRIMARY KEY (id);


--
-- Name: msg_pay_info msg_pay_info_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_pay_info
    ADD CONSTRAINT msg_pay_info_pkey PRIMARY KEY (id);


--
-- Name: msg_record msg_record_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_record
    ADD CONSTRAINT msg_record_pkey PRIMARY KEY (id);


--
-- Name: weixin_pay weixin_pay_pkey; Type: CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY weixin_pay
    ADD CONSTRAINT weixin_pay_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: msg_order_business_id_53def367; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX msg_order_business_id_53def367 ON msg_order USING btree (business_id);


--
-- Name: msg_pay_info_business_id_67a72616; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX msg_pay_info_business_id_67a72616 ON msg_pay_info USING btree (business_id);


--
-- Name: msg_record_business_id_bcca1ab7; Type: INDEX; Schema: public; Owner: cityking
--

CREATE INDEX msg_record_business_id_bcca1ab7 ON msg_record USING btree (business_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_order msg_order_business_id_53def367_fk_msg_business_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_order
    ADD CONSTRAINT msg_order_business_id_53def367_fk_msg_business_id FOREIGN KEY (business_id) REFERENCES msg_business(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_pay_info msg_pay_info_business_id_67a72616_fk_msg_business_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_pay_info
    ADD CONSTRAINT msg_pay_info_business_id_67a72616_fk_msg_business_id FOREIGN KEY (business_id) REFERENCES msg_business(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: msg_record msg_record_business_id_bcca1ab7_fk_msg_business_id; Type: FK CONSTRAINT; Schema: public; Owner: cityking
--

ALTER TABLE ONLY msg_record
    ADD CONSTRAINT msg_record_business_id_bcca1ab7_fk_msg_business_id FOREIGN KEY (business_id) REFERENCES msg_business(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

