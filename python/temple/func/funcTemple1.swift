        
        
        
        let hx_1 = "str1"
        var hx_str = ""
        switch hx_1 {
        case "str1":
            hx_str = "str1"
        case "str2":
            hx_str = "str2"
        case "str3":
            hx_str = "str2"
        case "str4":
            hx_str = "str2"
        case "str5":
            hx_str = "str2"
        case "str6":
            hx_str = "str2"
        default:
            hx_str = "str1"
            break
        }
        _ = NSArray(array: [hx_str])
        
        if hx_str == "str1" {
            let hx_att = [hx_str]
            _ = hx_att
        }
        else {
            let hx_att2 = [hx_str,hx_str,hx_str]
            _ = hx_att2
        }







