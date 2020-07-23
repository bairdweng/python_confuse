//
//  CFView3.swift
//  confusionExample
//
//  Created by bairdweng on 2020/5/25.
//  Copyright © 2020 bairdweng. All rights reserved.
//

import UIKit

class CFView3: UIView {
    var hx_dskView = UIScrollView()
    let hx_cfSwitch = CFSwitch()
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.addSubview(hx_dskView)
        hx_dskView.contentSize = CGSize(width: 20, height: 100)
        hx_dskView.contentInset = UIEdgeInsets.init(top: 10, left: 10, bottom: 10, right: 10)
        hx_dskView.alwaysBounceVertical = true
        hx_dskView.alwaysBounceHorizontal = true
        hx_dskView.addSubview(hx_cfSwitch)
        hx_initLabel2()
    }
    func hx_initLabel2() {
        let hx_title = UILabel()
        self.addSubview(hx_title)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}
