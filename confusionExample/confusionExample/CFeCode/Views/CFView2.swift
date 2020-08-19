//
//  CFView2.swift
//  confusionExample
//
//  Created by bairdweng on 2020/5/25.
//  Copyright © 2020 bairdweng. All rights reserved.
//

import UIKit

class CFView2: UIView {
    var hx_View2 = CFView3()
    override init(frame: CGRect) {
        super.init(frame: frame)
        let hx_model = CFModel()
        hx_model.hx_1 = "1"
        hx_model.hx_hellow = "2"
        hx_initLabel2()
    }
    func hx_initLabel2() {
        let hx_label = UILabel()
        hx_label.text = "Label"
        self.addSubview(hx_label)
        hx_label.frame = CGRect(x: 0, y: 0, width: self.frame.size.width/2, height: self.frame.size.height/3)
        hx_label.addSubview(hx_View2)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}
